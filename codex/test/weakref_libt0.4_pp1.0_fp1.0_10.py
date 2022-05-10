import weakref

from . import _ffi
from . import _lib
from . import _pycompat
from . import util
from . import encoding
from . import error


def _check_utf8(s):
    """Check if the given string is valid UTF-8.

    Returns True if so, False otherwise.
    """
    try:
        s.decode('utf-8')
    except UnicodeDecodeError:
        return False
    return True


def _check_utf8_list(list):
    """Check if the given list of strings are all valid UTF-8.

    Returns True if so, False otherwise.
    """
    for s in list:
        if not _check_utf8(s):
            return False
    return True


def _check_utf8_dict(dict):
    """Check if the given dict of strings are all valid UTF-8.

    Returns True if so, False otherwise.
    """
    for k, v in dict.items():
        if not _check_utf8(k) or not _check_utf8(v):
            return
