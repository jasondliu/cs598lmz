import _struct
import _thread
import _threading_local
import _time
import _token
import _tracemalloc
import _tracing
import _types
import _weakref
import _weakrefset
import _warnings
import _weakref
import _weakrefset
import _winapi
import _winreg
import _xxsubinterpreters

# Modules that need a custom initialization
# Order is important for bootstrapping reasons
# (some are based on previous ones, like _io is based on _collections)

# Optional modules
try:
    import _testcapi
except ImportError:
    pass

# Modules that are always enabled
import _abc
import _ast
import _bisect
import _blake2
import _codecs
import _collections
import _contextvars
import _csv
import _datetime
import _decimal
import _functools
import _hashlib
import _heapq
import _imp
import _io
import _json
import _locale
import _lsprof
import _md5
import _operator
import _pickle
