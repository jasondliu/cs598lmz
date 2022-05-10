import gc, weakref

from . import _glib, _gobject
from .utils import wrap_class
from .bindings import Binding, Signal, Property
from .factory import Factory
from . import signals

__all__ = []

_gobject._gobject_class_init(GObject)
_gobject._gobject_class_init(GInitiallyUnowned)
_gobject._gobject_class_init(GBoxed)
_gobject._gobject_class_init(GEnum)
_gobject._gobject_class_init(GFlags)
_gobject._gobject_class_init(GParamSpec)
_gobject._gobject_class_init(GType)

_gobject._gobject_class_init(GObjectClass)
_gobject._gobject_class_init(GInitiallyUnownedClass)
_gobject._gobject_class_init(GBoxedClass)
_gobject._gobject_class_init(GEnumClass)
_gobject._gobject_class_init(GFlagsClass)
_gobject._gobject_class
