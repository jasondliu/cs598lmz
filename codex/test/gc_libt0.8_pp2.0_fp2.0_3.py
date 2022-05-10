import gc, weakref
from types import FunctionType


class WeakMethod(object):
    """
    A callable class that proxies another callable, but does not prevent
    referential cycles from being reclaimed by the garbage collector.
    This is particularly useful for callbacks where a bound method
    is passed.
    """

    def __init__(self, inst, fun, proxy_type=None):
        if isinstance(fun, FunctionType):
            raise TypeError('expected a method, got a function')
        if proxy_type is None:
            if hasattr(fun, 'im_self'):
                proxy_type = weakref.ProxyTypes.ReferenceType
            else:
                proxy_type = weakref.ProxyTypes.CallableProxyType
        ref_inst = weakref.proxy(inst, proxy_type)
