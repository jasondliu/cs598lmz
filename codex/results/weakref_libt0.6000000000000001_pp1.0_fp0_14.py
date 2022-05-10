import weakref
from zope.interface import implementer
from zope.interface import implementer_only
from zope.interface.interface import InterfaceClass
from zope.interface.interfaces import IInterface
from zope.interface.interfaces import IMethod
from zope.interface.interfaces import IObjectEvent
from zope.interface.interfaces import ObjectEvent
from zope.interface.interfaces import ObjectSpecificationDescriptor

import cyordereddict as cyodict
import cyordereddict.ordereddict as cyodict_ordereddict
import cyordereddict.ordereddict as cyodict_ordereddict_ext

__all__ = [
    'Interface', 'Attribute', 'Method',
    'implementedBy', 'implementedByInstancesOf', 'directlyProvides',
    'classImplements', 'moduleProvides',
    'provides', 'classProvides',
    'alsoProvides',
    'noLongerProvides', 'declareImplementation',
    'directlyProvidedBy', 'providedBy',
    'adapter_hooks', 'queryAdapter'
    ]
