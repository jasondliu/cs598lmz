import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import logging
import os
import sys
import time
import traceback
import uuid
import weakref

from . import _base
from . import _compat
from . import _constants
from . import _errors
from . import _events
from . import _ffi
from . import _util
from . import _version
from . import _virtualtables
from . import _vtshim
from . import _wal
from . import _walreceiver
from . import _walwriter
from . import _xlog

_logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# The following constant is used to determine the maximum length of a string
# or BLOB in bytes which can be used safely in SQLite.

try:
    SQLITE_MAX_LENGTH = _ffi.SQLITE_MAX_LENGTH
except AttributeError:
    # SQLite 3.8.3 and earlier
    SQLITE_MAX_LENGTH = 1000000000

# -----------------------------------------------------------------------------
# The following constant is used to determine the maximum length of a string
# or
