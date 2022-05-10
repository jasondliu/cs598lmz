import weakref

from zope.interface import implements
from zope.component import adapts
from zope.component import queryUtility
from zope.component import getUtilitiesFor
from zope.component import getAdapter
from zope.component.interfaces import IFactory
from zope.component.factory import Factory
from zope.component.persistentregistry import PersistentAdapterRegistry
from zope.component.persistentregistry import PersistentComponents
from zope.component.interfaces import IAdapterRegistration
from zope.component.interfaces import IFactoryRegistration
from zope.component.interfaces import IComponentLookup
from zope.component.interfaces import IComponentRegistry
from zope.component.interfaces import ISite
from zope.component.interfaces import IAdapterFactory
from zope.component.interfaces import IHandlerRegistration
from zope.component.interfaces import IHandlerFactory
from zope.component.interfaces import IHandler
from zope.component.interfaces import IRegistration
from zope.component.interfaces import ComponentLookupError
from zope.component.inter
