import gc, weakref
from . import _compat
from . import _gc_interface
from . import _weakref_backport
from . import _weakref_helper
from . import _weakrefset
from . import _weakref_proxy

from . import _weakref_helper
from . import _weakref_backport
from . import _weakrefset
from . import _weakref_proxy
from . import _compat
from . import _gc_interface
from ._weakref_helper import CallableProxyType, ProxyType, _remove_dead_weakref
from ._weakref_helper import _IterationGuard
from ._weakref_helper import ref
from ._weakref_helper import ReferenceType
from ._weakref_helper import getweakrefcount
from ._weakref_helper import getweakrefs
from ._weakref_helper import ProxyTypes
from ._weakref_helper import WeakMethod
from ._weakref_helper import WeakMethodProxy
from ._weakref_helper import WeakMethodProxyType
from ._weakref_backport import WeakSet
from ._weakref_backport
