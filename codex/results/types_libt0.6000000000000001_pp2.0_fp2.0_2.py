import types
types.NoneType = type(None) # for python 2.5

from . import _gobject

from .pygobject import pygobject_new
from .pygobject import pygobject_register_sinkfunc
from .pygobject import pygobject_register_class_init
from .pygobject import pygobject_register_wrapper
from .pygobject import pygobject_lookup_class
from .pygobject import pygobject_set_has_new_constructor
from .pygobject import pygobject_set_has_weak_ref
from .pygobject import pygobject_new_full
from .pygobject import pygobject_new_with_properties

from .pygobject import \
     pygobject_set_constructor_need_type, \
     pygobject_set_constructor_need_type_init, \
     pygobject_set_constructor_need_new_init

from .pygobject import \
     pygobject_set_class_metadata, \
     pygobject_set_class_metadata_
