import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref
import _weakrefset

# Modules that are optional and may not be present
_collections_abc = None
_functools = None
_imp = None
_io = None
_locale = None
_operator = None
_pickle = None
_random = None
_socket = None
_sre = None
_stat = None
_string = None
_symtable = None
_testcapi = None
_threading_local = None
_tracemalloc = None
_warnings = None
_weakref = None
_weakrefset = None

try:
    import _collections_abc
except ImportError:
    pass

try:
    import _functools
except ImportError:
    pass

try:
    import _imp
except ImportError:
    pass

try:
    import _io
except ImportError:
    pass

try:
    import _locale
except ImportError:
