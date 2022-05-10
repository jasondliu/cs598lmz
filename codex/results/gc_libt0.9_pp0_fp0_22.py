import gc, weakref, types, sys

from kiwi.utils import gsignal
from kiwi.environ import environ

class SimpleRef(object):
    def __init__(self, proxy):
        self.ref = weakref.ref(proxy)
        self.func = None

    def set_finalize_func(self, func):
        self.func = func

    def finalize(self):
        if self.func:
            self.func()


def remove_object(object):
    for weak in (ob for ob in gc.get_referrers(object)
                 if type(ob) is SimpleRef):
        object = weak.ref
        if object is not None:
            object._destroy()


class Proxy(object):
    __gproperties__ = {'object': (object, 'object which owns the wrapper',
                                  'The wrapped gobject, which internally '
                                  'should be a GObject',
                                  gobject.PARAM_READWRITE)}

    __gproperties__.update(
        ProxyMeta.__gproperties__)

    __
