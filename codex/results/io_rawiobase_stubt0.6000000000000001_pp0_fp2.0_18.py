import io
class File(io.RawIOBase):
    ...
class Stream(io.RawIOBase):
    ...
class TextIOWrapper(io.TextIOBase):
    ...
class StringIO(io.StringIOBase):
    ...
class BytesIO(io.BytesIO):
    ...

try:
    import thread
except ImportError:
    import _thread as thread

import builtins as __builtin__

def abs(x):
    """
    Return the absolute value of the argument.
    """
    return __builtin__.abs(x)

def all(iterable):
    """
    Return True if bool(x) is True for all values x in the iterable.
    """
    return __builtin__.all(iterable)

def any(iterable):
    """
    Return True if bool(x) is True for any x in the iterable.
    """
    return __builtin__.any(iterable)

def ascii(obj):
    """
    As repr(), return a string containing a printable representation of an
    object, but escape the non-ASC
