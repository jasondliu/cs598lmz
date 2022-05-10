import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# The following modules are not builtin, but are always available.
import _codecs
import _collections
import _functools
import _imp
import _io
import _locale
import _operator
import _signal
import _sre
import _stat
import _string
import _symtable
import _thread
import _warnings
import _weakref

# These modules are builtin, but are optional.
try:
    import _ast
except ImportError:
    pass

try:
    import _bisect
except ImportError:
    pass

try:
    import _bytesio
except ImportError:
    pass

try:
    import _contextvars
except ImportError:
    pass

try:
    import _datetime
except ImportError:
    pass

try:
    import _elementtree
except ImportError:
    pass

try:
    import _heapq
except ImportError:
