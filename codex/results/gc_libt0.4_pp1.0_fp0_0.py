import gc, weakref
from weakref import WeakKeyDictionary
from ctypes import *
from ctypes.util import find_library

from . import _lib, _ffi, _ffi_lib, _gobject, _gobject_lib

from .utils import _wrap_constructor, _wrap_function, _wrap_method, _wrap_property, _wrap_property_ro, _wrap_property_wo

_gobject_lib.g_object_ref_sink.restype = c_void_p
_gobject_lib.g_object_ref_sink.argtypes = [c_void_p]

_gobject_lib.g_object_class_find_property.restype = _gobject.GParamSpec
_gobject_lib.g_object_class_find_property.argtypes = [_gobject.GObjectClass, c_char_p]

_gobject_lib.g_object_class_list_properties.restype = _ffi.CDataPtr
_gobject_lib.g_object_class_list_properties.argtypes = [
