import weakref

from . import _cffi_backend
from . import _ctypes_backend
from . import _cython_backend
from . import _dlfcn_backend
from . import _ctypes_backend
from . import _dlopen_backend
from . import _lazy_dlopen_backend
from . import _osx_backend
from . import _windows_backend

from ._backend import (
    Backend,
    Library,
    CDLL,
    PyDLL,
    LibraryLoader,
    get_errno,
    set_errno,
    reset_errno,
    get_last_error,
    set_last_error,
    reset_last_error,
    format_error,
    set_converters,
    set_com_error_handler,
    set_faulthandler_enabled,
    set_faulthandler_disabled,
    set_faulthandler_dump_traceback,
    set_faulthandler_dump_traceback_later,

