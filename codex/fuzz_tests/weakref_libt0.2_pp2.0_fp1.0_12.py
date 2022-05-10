import weakref

from . import _ffi as ffi
from . import _lib as lib
from . import _util as util
from . import _errors as errors
from . import _types as types
from . import _constants as constants
from . import _cdata as cdata
from . import _enums as enums
from . import _functions as functions
from . import _structs as structs
from . import _classes as classes
from . import _methods as methods
from . import _properties as properties
from . import _interfaces as interfaces
from . import _signals as signals
from . import _vfuncs as vfuncs
from . import _deprecated as deprecated
from . import _version as version

__all__ = []

def _init():
    # Initialize GObject
    lib.g_type_init()
    # Initialize Gtk
    lib.gtk_init(ffi.NULL, ffi.NULL)

_init()

def _get_type_name(gtype):
    return ffi.string(lib.g_type_name(gtype
