import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# The following modules are defined but not imported by the standard library.
# They are defined here so that they can be imported by other modules.
import _abc
import _ast
import _codecs
import _collections_abc
import _contextvars
import _functools
import _io
import _locale
import _operator
import _signal
import _sre
import _stat
import _string
import _symtable
import _tracemalloc
import _weakref

# Importing _dummy_threading is optional.
try:
    import _dummy_threading
except ImportError:
    pass

# Importing _markupbase is optional.
try:
    import _markupbase
except ImportError:
    pass

# Importing _winreg is optional.
try:
    import _winreg
except ImportError:
    pass

# Importing _lsprof is optional.
try:
    import _
