# -*- coding: utf-8 -*-

from Products.CMFCore.permissions import setDefaultRoles

PROJECTNAME = 'collective.periodcriterion'

ADD_PERMISSIONS = {
    'ATPeriodCriteria': "%s: Add ATPeriodCriteria" % PROJECTNAME
}

for permission in ADD_PERMISSIONS.values():
    setDefaultRoles(permission, ('Manager',))

