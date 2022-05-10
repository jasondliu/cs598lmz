import _struct
import _thread

# ______________________________________________________________________

def get_errno():
    """Returns the current value of the C library's errno variable."""
    return _ctypes.get_errno()

# ______________________________________________________________________

def strerror(errno):
    """Given an error code, return a string describing the error.

    This is a wrapper around the C library function strerror().
    """
    return _ctypes.strerror(errno)

def perror(message):
    """Write a string describing the current errno value to stderr.

    This is a wrapper around the C library function perror().
    """
    return _ctypes.perror(message)

# ______________________________________________________________________

def _check_null(result, func, args):
    """Return an error if the result of a ctypes call is a NULL pointer."""
    if not result:
        raise OSError(get_errno(), strerror(get_errno()))
    return result

# ______________________________________________________________________

