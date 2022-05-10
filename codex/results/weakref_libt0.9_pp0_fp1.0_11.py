import weakref
import traceback
import types

from zope.interface import implements
from zope.component import adapts
from zope.event import notify
from zope.lifecycleevent import ObjectCreatedEvent

from Acquisition import aq_base

import Products.ZCatalog
from Products.Five.event import notifyHandlerInitialized
from Products.CMFCore.utils import UniqueObject

from Products.ATContentTypes.interfaces import (
    IATFolder, IConstrainTypes, IATTopic)
from Products.ATContentTypes.permission import (
    EditTopics, ChangeTopics, ModifyConstrainTypes)
from Products.ATContentTypes.content.topic import (
    ATTopic, ATTopicCriterion)
from Products.ATContentTypes.criteria import registerCriterion

from plone.app.collection.interfaces import ICollection
from plone.app.collection.events import CollectionModifiedEvent

ATFolderSchema = ATTopic.schema

# add field for constraint of contained types
constraintypesfield = LinesField(
    'constrainTypesMode',
    required=False,

