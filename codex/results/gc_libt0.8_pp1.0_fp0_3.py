import gc, weakref, lxml.etree
from collections import defaultdict
from warnings import warn

import xpybutil.util as util
import xpybutil.ewmh as ewmh
import xpybutil.event as event
import xpybutil.ewmh as ewmh
import xpybutil.icccm as icccm
import xpybutil.wm as wm
import xpybutil.render as render
import xpybutil.dpy as dpy

def lazyprop(fn):
    attr_name = '_lazy_' + fn.__name__

    def getter(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(getter)

class Window(object):
    def __new__(cls, wid=None, keep=False):
        value = cls.__dict__.get('__new__', object.__new__)
        if value is object.__
