import _struct
import _thread
import _threading
import _time
import _traceback
import _warnings
import _weakref

# Modules that are optional and may not be present
_collections_abc = None
_functools = None
_imp = None
_io = None
_locale = None
_operator = None
_posixsubprocess = None
_signal = None
_stat = None
_symtable = None
_thread = None
_tracemalloc = None
_winreg = None

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
    pass

try:
    import _operator
except ImportError:
    pass

try:
    import _posixsubprocess
except ImportError:
    pass

try:
   
