import ctypes
import ctypes.util
import threading
import sqlite3

try:
    from . import _lib
except ImportError:
    _lib = None

from . import _util

from . import _const
from . import _error
from . import _exception
from . import _lib
from . import _types
from . import _util

_logger = _util.get_logger(__name__)

#
# Global variables
#

_g_lock = threading.Lock()

_g_lib = None

_g_initialized = False
_g_initialized_lock = threading.Lock()

_g_db = None
_g_db_lock = threading.Lock()

_g_db_path = None
_g_db_path_lock = threading.Lock()

_g_db_connection = None
_g_db_connection_lock = threading.Lock()

_g_db_cursor = None
_g_db_cursor_lock = threading.Lock()

_g_db_transaction_count = 0
_g_db_transaction_
