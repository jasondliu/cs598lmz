import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:').execute("CREATE TABLE test (id INTEGER PRIMARY KEY)")

from . import _common as c


# This is the gpgme_*_t type for gpgme_ctx_t.
# See:
#  https://www.gnupg.org/documentation/manuals/gpgme/Context-Types.html#Context-Types
_ctx_t = ctypes.c_void_p


# gpgme_keylist_mode_t
# See:
#  https://www.gnupg.org/documentation/manuals/gpgme/Key-Listing.html#Key-Listing
_keylist_mode_t = ctypes.c_uint
_keylist_mode_t.__doc__ = '''
Key listing mode.

Note: GPGME is a C library, so C-style enums are used here.
'''
GPGME_KEYLIST_MODE_LOCAL = 0
GPGME_KEYLIST_MODE_EXTERN = 1
GPGME_KEYLIST_MODE_
