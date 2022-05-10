import gc, weakref, threading
from _weakrefset import WeakSet


from weakref import ref as _ref
from weakref import CallableProxyType as _CallableProxyType
from weakref import ProxyType as _ProxyType
from weakref import getweakrefcount as _getweakrefcount
from weakref import getweakrefs as _getweakrefs

