import _struct
import _sys
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# Importing the _ast module triggers parsing of the grammar.
# This is needed because some of the code below assumes that the
# parsing has already been done.
import _ast

# Import these here so they get registered in sys.modules.
import builtins
import copyreg
import abc
import _weakrefset

# Enable meta path based loader if not already enabled
try:
    import builtin_meta
except ImportError:
    pass

_setup()

# The built-in open function is replaced by io.open().
# This is done first so that we don't load the io module for nothing.
def open(file, mode="r", buffering=-1, encoding=None,
         errors=None, newline=None, closefd=True, opener=None):
    """Open file and return a stream.  Raise IOError upon failure.

    file is either a text or byte string giving the name (and the path
    if
