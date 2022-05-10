import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for a bug in Python 2.7.3
# See http://bugs.python.org/issue15881#msg170215
try:
    import thread
except ImportError:
    import _thread as thread

from . import _cffi_backend
from . import _cffi_include
from . import _cffi_errors
from . import _cffi_utils
from . import _cffi_types
from . import _cffi_exports
from . import _cffi_mallocs
from . import _cffi_build
from . import _cffi_unstub
from . import _cffi_cdef
from . import _cffi_parse
from . import _cffi_setup
from . import _cffi_test
from . import _cffi_dlfcn
from . import _cffi_callbacks
from . import _cffi_include_emulation
from . import _cffi_types_backend
from
