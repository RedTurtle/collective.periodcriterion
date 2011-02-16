  # -*- extra stuff goes here -*- 

from zope.i18nmessageid import MessageFactory
from collective.periodcriterion import config

from Products.Archetypes import atapi
from Products.CMFCore import utils

periodCriterionMessageFactory = MessageFactory('collective.periodcriterion')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    import criteria
    
    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
            content_types=(atype,),
            permission=config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
            ).initialize(context)