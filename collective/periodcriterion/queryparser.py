# -*- coding: utf-8 -*-

from DateTime import DateTime

from plone.app.querystring.queryparser import Row
from plone.app.querystring.queryparser import _between

from .criteria import getBounds

def _this_month(context, row):
    now = DateTime()
    row = Row(index=row.index,
              operator=row.operator,
              values=getBounds(now, 'this_month'))
    return _between(context, row)

def _this_year(context, row):
    now = DateTime()
    row = Row(index=row.index,
              operator=row.operator,
              values=getBounds(now, 'this_year'))
    return _between(context, row)
