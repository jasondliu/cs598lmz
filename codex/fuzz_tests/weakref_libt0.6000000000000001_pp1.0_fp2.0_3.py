import weakref

from . import _gobject
from . import _glib

def _get_property(gobj, name):
    return gobj.get_property(name)

def _set_property(gobj, name, value):
    gobj.set_property(name, value)

def _call(gobj, name, *args):
    return gobj.__getattribute__(name)(*args)

def _get_value(gobj, name):
    return gobj.__getattribute__(name).get_value()

def _set_value(gobj, name, value):
    gobj.__getattribute__(name).set_value(value)

_signal_new = _gobject.signal_new

def _signal_lookup(gobj, name, detail=None):
    if detail is not None:
        name = '%s::%s' % (name, detail)
    return _gobject.signal_lookup(name, gobj.__class__)

def _signal_connect(gobj,
