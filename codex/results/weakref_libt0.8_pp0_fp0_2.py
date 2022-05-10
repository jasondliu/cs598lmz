import weakref
from zope import interface
from zope import component

from z3c.table import interfaces
from z3c.table import column
from z3c.table import table
from z3c.table import value
from z3c.table.column import ColumnTableMixin
from z3c.table import batch
from z3c.table.testing import TestRequest

from zope.app.testing import ztapi
from zope.app.testing import setup
from zope.app.testing.placelesssetup import setUp as setUpTestSite
from zope.app.testing.placelesssetup import tearDown as tearDownTestSite
from zope.component.testing import setUp as setUpComponent
from zope.component.testing import tearDown as tearDownComponent


class IBlah(interface.Interface):
    pass

class IBlub(interface.Interface):
    pass

class Blah(object):
    interface.implements(IBlah)

class Blub(object):
    interface.implements(IBlub)


def setUp(test=
