import ctypes
import ctypes.util
import threading
import sqlite3
import re

from . import _libxml2mod

#
# Module globals
#
_thread_lock = threading.RLock()
_thread_context = threading.local()

#
# Exceptions
#
class XMLSchemaParseError(Exception):
    """
    Exception raised when a Schema instance is created from a string
    and the string is not a valid XML Schema document.
    """
    pass

class XMLSchemaValidateError(Exception):
    """
    Exception raised when a Document instance fails to validate against
    its schema.
    """
    pass

#
# Utility functions
#
def _decode_string(s):
    """
    Decode a string from bytes to unicode.
    """
    if isinstance(s, bytes):
        encoding = sys.getfilesystemencoding()
        s = s.decode(encoding)
    return s

def _encode_string(s):
    """
    Encode a string from unicode to bytes.
    """
    if isinstance(s, str):
