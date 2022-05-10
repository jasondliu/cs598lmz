import weakref

from . import _cffi_backend
from . import _ctypes_backend
from . import _cython_backend
from . import _dlfcn_backend
from . import _libraries
from . import _loader
from . import _osx_support
from . import _posix
from . import _util
from . import _windows
from . import _winreg_backend

__all__ = [
    'CDLL', 'PyDLL', 'OleDLL', 'WinDLL', 'LibraryLoader', 'get_loader',
    'load_library', 'load', 'get_library_file', 'get_libraries',
    'get_library_names', 'get_library_full_path', 'get_symbols',
    'get_symbol_names', 'get_symbol_version', 'get_symbol_alias',
    'get_symbol_address', 'has_symbol', 'has_symbols', 'get_symbol',
    'get_symbols_by_version', 'get_symbols
