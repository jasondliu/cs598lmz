import gc, weakref, collections
from weakref import WeakKeyDictionary
import logging
import pprint

from zope.interface import implements
from zope.component import getUtility

from Products.CMFCore.utils import getToolByName

from collective.transmogrifier.interfaces import ISection, ISectionBlueprint
from collective.transmogrifier.utils import defaultMatcher
from collective.transmogrifier.utils import Expression, Condition, ConditionError

from collective.alias.logger import logger


class AliasCondition(Condition):
    """ This condition is used in the blueprint to determine if we need to set an alias
    """

    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.transmogrifier = transmogrifier
        self.name = name
        self.previous = previous
        self.pathkey = defaultMatcher(options, 'path-key', name, 'path')
        self.condition = Expression(
            defaultMatcher(options, '
