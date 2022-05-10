import ctypes
import ctypes.util
import threading
import sqlite3

logger = logging.getLogger(__name__)

#### Constants
SQLITE_OPEN_READONLY = 0x00000001
SQLITE_OPEN_READWRITE = 0x00000002
SQLITE_OPEN_CREATE = 0x00000004
SQLITE_OPEN_MEMORY = 0x00002000
SQLITE_OPEN_NOMUTEX = 0x00008000
SQLITE_OPEN_FULLMUTEX = 0x00010000
SQLITE_OPEN_SHAREDCACHE = 0x00020000
SQLITE_OPEN_PRIVATECACHE = 0x00040000

SQLITE_TYPES = {
    'integer': ('integer', 'int', 'int32', 'int64', 'long', 'short'),
    'float': ('real', 'double', 'double precision'),
    'text': ('text',),
    'blob': ('blob', 'binary'),
    'unknown': ('null', 'numeric', 'boolean'),
}

SQLITE_COLUMN_TYPES = list(
