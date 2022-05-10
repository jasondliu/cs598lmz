import gc, weakref

from zope.interface import Interface, implements
from zope.component import adapts, getUtility, getMultiAdapter
from zope.component.interfaces import IFactory
from zope.component.factory import Factory
from zope.component.interfaces import ComponentLookupError
from zope.component.hooks import getSite
from zope.container.interfaces import IObjectAddedEvent
from zope.container.interfaces import IObjectRemovedEvent
from zope.container.interfaces import IObjectMovedEvent
from zope.container.interfaces import IContainerModifiedEvent
from zope.container.interfaces import IContainer
from zope.container.contained import notifyContainerModified
from zope.container.interfaces import IContained
from zope.container.interfaces import IWriteContainer
from zope.container.interfaces import IReadContainer
from zope.container.interfaces import IItemContainer
from zope.container.interfaces import IContainerNamesContainer
from zope.container.interfaces import IContainerNames
from zope.container.interfaces import IContainerSublocations

