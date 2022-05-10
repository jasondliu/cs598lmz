import gc, weakref, threading
from _weakrefset import WeakSet


from weakref import ref as _ref
from weakref import CallableProxyType as _CallableProxyType
from weakref import ProxyType as _ProxyType
from weakref import getweakrefcount as _getweakrefcount
from weakref import getweakrefs as _getweakrefs

from cppyy.ll import nullptr

from .core import CPPMeta
from .utils import make_function_forwarder
from .gbl import gbl
gbl.add_operators(globals())


#
# weak referencing support
#

_weakref_support_namespace = []
class WeakMethod(object):
    """Simple thin wrapper to allow weak references to bound methods."""
    __slots__ = ["fn_ref", "meth_type", "inst_ref"]

    def __new__(cls, method, callback=None):
        try:
            obj = _ref(method.__self__, callback)
        except TypeError:
            pass
        else:
            if method.__self__ is None
