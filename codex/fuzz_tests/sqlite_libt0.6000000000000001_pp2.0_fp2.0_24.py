import ctypes
import ctypes.util
import threading
import sqlite3
from datetime import datetime
from time import time
from enum import Enum

from . import _lib
from . import _util
from . import _const
from . import _error
from . import _compat
from . import _props
from . import _connection
from . import _statement
from . import _transaction
from . import _backup
from . import _cursor
from . import _trace
from . import _progress
from . import _atomics
from . import _prepare
from . import _vfs
from . import _loadext

_lib.sqlite3_initialize()

_lib.sqlite3_enable_shared_cache(1)

_lib.sqlite3_config(ctypes.c_int(_const.SQLITE_CONFIG_SINGLETHREAD))

_lib.sqlite3_config(ctypes.c_int(_const.SQLITE_CONFIG_LOG),
                    _trace.sqlite3_log_callback)

_lib.sqlite3_config(ctypes.c_int(_const.SQLITE
