import weakref
from zope.interface import Interface, Attribute, implements
from zope.interface.common.mapping import IItemMapping, IFullMapping
from zope.component.interfaces import IObjectEvent
from zope.component.interfaces import IObjectEventSubscription, IHandler
from zope.component.interfaces import IObjectEventDispatcher, IObjectEventHandler
from zope.component.interfaces import IComponentArchitecture
from zope.component.interfaces import ObjectEventNotSupported
from zope.component.interfaces import IObjectEventDescription
from zope.component.interfaces import ComponentLookupError
from zope.component.interfaces import IInterface
from zope.interface import InterfaceClass
from zope.interface.interfaces import IInterfaceDeclaration
from zope.interface.interfaces import IObjectEvent as IZopeObjectEvent
from zope.interface.interfaces import IObjectEventPublication
from zope.interface.interfaces import IObjectEventSubscription as IZopeObjectEventSubscription
from zope.interface.interfaces import IObjectEventHandler as IZopeObjectEvent
