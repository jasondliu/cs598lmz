import _struct
import _sys
import _types
import _warnings
import _weakref
import _weakrefset

# Only import these modules if they are actually used.
# This is to work around circular dependencies.
_collections = None
_functools = None
_heapq = None
_io = None
_locale = None
_random = None
_socket = None
_sre = None
_stat = None
_symtable = None
_thread = None
_tracemalloc = None
_warnings = None

# Import the sys module separately from the builtins, so that we can
# store the original value of sys.modules in the builtins.
import sys as _sys

# Set sys.modules so that we can import builtin modules.
_sys.modules['builtins'] = _sys.modules['__main__']

# Import builtin modules.
import _thread
import _warnings

# Import the builtin exceptions.
from exceptions import *

# Import the warnings module, to raise warnings.
import warnings as _warnings

# Import the abc module
