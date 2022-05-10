import weakref
import zope.interface
import zope.component

from zope.component.interfaces import IFactory
from zope.component.globalregistry import BaseGlobalComponents
from zope.component.registry import Components
from zope.component.registry import UtilityRegistration
from zope.component.registry import AdapterRegistration
from zope.component.registry import SubscriptionRegistration
from zope.component.registry import HandlerRegistration
from zope.component.registry import queryMultiAdapter, queryAdapter, \
                                    queryAdapterInContext, queryMultiAdapterInContext
from zope.component.registry import getUtility
from zope.component.registry import queryUtility
from zope.component.registry import getUtilitiesFor, getAllUtilitiesRegisteredFor
from zope.component.registry import getAdapters, getMultiAdapter
from zope.component.registry import subscribers, getSubscriptionAdapter
from zope.component.registry import getHandler
from zope.component.registry import SiteManagerContainer
from zope.component.registry import AdapterRegistry
