import weakref

from . import _cffi_backend
from . import _ctypes_backend
from . import _cython_backend
from . import _dlfcn_backend
from . import _ctypes_backend
from . import _dl_backend
from . import _libraries
from . import _loader
from . import _osx_support
from . import _posix
from . import _util

__all__ = [
    'CDLL', 'PyDLL', 'OleDLL', 'WinDLL', 'LibraryLoader', 'load_library',
    'get_errno', 'set_errno', 'get_last_error', 'set_last_error',
    'get_string_encoding', 'set_string_encoding',
    'set_conversion_mode', 'get_conversion_mode',
    'set_com_error_handler', 'get_com_error_handler',
    'set_com_error_handle_mode', 'get_com_error_handle_mode',
    'set_fmod', 'get_
