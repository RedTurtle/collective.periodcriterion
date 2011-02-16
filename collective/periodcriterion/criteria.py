# -*- coding: utf-8 -*-

from DateTime import DateTime
from zope.interface import implements
from Products.Archetypes import atapi
from AccessControl import ClassSecurityInfo
from Products.CMFCore import permissions

from Products.ATContentTypes.criteria.schemata import ATBaseCriterionSchema
from Products.ATContentTypes.criteria.base import ATBaseCriterion
from Products.ATContentTypes.criteria import registerCriterion
from Products.ATContentTypes.criteria import DATE_INDICES
from Products.ATContentTypes.interfaces import IATTopicSearchCriterion
from Products.ATContentTypes.permission import ChangeTopics

from collective.periodcriterion import periodCriterionMessageFactory as _
from collective.periodcriterion.interfaces import IATPeriodCriteria

def getBounds(date, value):
    """
        Obtain two bound dates, based on the current date and value used
        
        >>> from collective.periodcriterion.criteria import getBounds
        >>> from DateTime import DateTime
        >>> getBounds(DateTime('2011/02/14'), 'today')
        (DateTime('2011/02/14'), DateTime('2011/02/14 23:59:59 GMT+1'))

        Hour is ignored completly
        
        >>> getBounds(DateTime('2011/02/14 23:59:59'), 'today')
        (DateTime('2011/02/14'), DateTime('2011/02/14 23:59:59 GMT+1'))
        
        Check month

        >>> getBounds(DateTime('2011/02/14'), 'this_month')
        (DateTime('2011/02/01'), DateTime('2011/02/28 23:59:59 GMT+1'))
        >>> getBounds(DateTime('2011/02/01'), 'this_month')
        (DateTime('2011/02/01'), DateTime('2011/02/28 23:59:59 GMT+1'))
        >>> getBounds(DateTime('2011/02/28'), 'this_month')
        (DateTime('2011/02/01'), DateTime('2011/02/28 23:59:59 GMT+1'))
        >>> getBounds(DateTime('2011/12/25'), 'this_month')
        (DateTime('2011/12/01'), DateTime('2011/12/31 23:59:59 GMT+1'))

        Check year

        >>> getBounds(DateTime('2011/02/02'), 'this_year')
        (DateTime('2011/01/01'), DateTime('2011/12/31 23:59:59 GMT+1'))


    """
    if value=='today':
        today = DateTime(date.Date())
        return (today, DateTime(today.strftime('%Y/%m/%d')+' 23:59:59'))
    elif value=='this_month':
        month_start = DateTime('%d/%02d/01' % (date.year(), date.month()) )
        nextMonth = date.month()+1
        year = date.year()
        if nextMonth==13:
            year+=1
            nextMonth = 1
        return (month_start, DateTime('%d/%02d/01 23:59:59' % (year, nextMonth) )-1 )
    elif value=='this_year':
        return (DateTime('%d/01/01' % date.year()), DateTime('%d/12/31 23:59:59' % date.year()) )            
    return ()


periodVocabulary = atapi.DisplayList((
    ('today', _(u'Today')),
    ('this_month', _(u'This month')),
    ('this_year', _(u'This year')),
    ))

PeriodCriteriaSchema = ATBaseCriterionSchema + atapi.Schema((
    atapi.StringField('period',
                required=1,
                write_permission=ChangeTopics,
                default='today',
                vocabulary=periodVocabulary,
                widget=atapi.SelectionWidget(
                    label=_(u'label_date_criteria_value', default=u'Which period'),
                    description=_(u'help_date_criteria_value',
                                  default=u'Select the period inside which the date must be.')
                    ),
                ),
    ))

class ATPeriodCriteria(ATBaseCriterion):
    """A relative date criterion"""

    implements(IATPeriodCriteria)
    __implements__ = ATBaseCriterion.__implements__ + (IATTopicSearchCriterion, )

    security       = ClassSecurityInfo()
    schema         = PeriodCriteriaSchema
    meta_type      = 'ATPeriodCriteria'
    archetype_name = 'Period Date Criteria'
    shortDesc      = _(u'Period of time')


    security.declareProtected(permissions.View, 'Value')
    def Value(self):
        now = DateTime()
        value = self.getPeriod()
        return getBounds(now, value)

    security.declareProtected(permissions.View, 'getCriteriaItems')
    def getCriteriaItems(self):
        """Return a sequence of items to be used to build the catalog query.
        """
        field = self.Field()
        value = self.Value()

        return ( ( field, {'query': value, 'range': 'min:max'} ), )
    

registerCriterion(ATPeriodCriteria, DATE_INDICES)
