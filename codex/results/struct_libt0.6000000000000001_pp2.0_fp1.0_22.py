import _struct
import _thread
import _time
import _types
import _weakref

# The following modules are written by hand:
import _functools
import _io
import _locale
import _operator
import _signal
import _socket
import _sre
import _stat
import _string
import _symtable
import _threading
import _tracemalloc
import _warnings
import array
import errno
import faulthandler
import future_builtins
import itertools
import marshal
import math
import operator
import sys
import time
import xxsubtype

# Disable the garbage collector (if possible)
try:
    import gc
except ImportError:
    pass
else:
    gc.disable()
    gc.collect()

# The _warnings module is bootstrapped in Python/Python-ast.c::PyAST_Compile()
# and cannot be imported normally.
_warnings.onceregistry = {}
try:
    _warnings.oncekey
except AttributeError:
    _warnings.oncekey = _warnings
