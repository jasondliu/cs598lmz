import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

from . import sqlite_utils
from . import sqlite_utils_ex

from . import sqlite_utils_config
from . import sqlite_utils_support

from . import sqlite_utils_exception
from . import sqlite_utils_logging

# from . import sqlite_utils_debug

#
#
#

# SQLITE_ENABLE_STAT4 = 0x00000010     /* Enable SQLITE_STMTSTATUS_SORT */
# SQLITE_ENABLE_STAT3 = 0x00000008     /* Enable SQLITE_STMTSTATUS_AUTOINDEX */
# SQLITE_ENABLE_STAT2 = 0x00000004     /* Enable SQLITE_STMTSTATUS_VM_STEP */
# SQLITE_ENABLE_STAT1 = 0x00000002     /* Enable SQLITE_STMTSTATUS_FULLSCAN_STEP */
# SQLITE_ENABLE_STAT0 = 0x00000001     /* Enable SQLITE_STMTSTATUS_REPLACE */

# SQLITE_STATUS_MALLOC_C
