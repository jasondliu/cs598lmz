import gc, weakref

from . import _core
from ._core import ffi, lib
from . import _util
from ._util import _check_null, _check_ffi_error, _check_ffi_return
from . import _error
from ._error import Error
from . import _object
from ._object import Object
from . import _class
from ._class import Class
from . import _method
from ._method import Method
from . import _property
from ._property import Property
from . import _signal
from ._signal import Signal
from . import _value
from ._value import Value
from . import _closure
from ._closure import Closure

_gobject_module = None

def _init():
    global _gobject_module

    if _gobject_module is None:
        _gobject_module = _core.get_module('GObject')
        _gobject_module.register_types()

    _gobject_module.ensure_object_types_registered()

def _init_gobject():
    _init()
    _check_ffi_error(lib.g_
