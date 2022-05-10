import ctypes
import ctypes.util
import threading
import sqlite3
import time

from ctypes import c_int, c_uint, c_char_p, c_void_p, c_size_t, c_uint32, c_uint64, c_double, c_int32, c_int64, c_bool
from ctypes import Structure, Union, POINTER, pointer, cast, create_string_buffer, addressof
from ctypes import CFUNCTYPE, py_object

from . import _lib
from . import _ffi
from . import _rawffi
from . import _ctypes_patch
from . import _utils
from . import _errors
from . import _transaction_impl
from . import _database_impl
from . import _statement_impl
from . import _cursor_impl
from . import _backup_impl

_lib.sqlite3_enable_shared_cache(1)

#==============================================================================
# Exceptions
#==============================================================================

class Error(Exception):
    """Base class for all database exceptions."""
    pass

class Warning(Exception):
    """Base class for all database
