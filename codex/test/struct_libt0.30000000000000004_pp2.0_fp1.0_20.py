import _struct
import _sys
import _thread
import _time
import _types
import _warnings
import _weakref
import _zipfile
import _zlib

# The following modules are written in Python.
# They have to be imported last because they may import _io or _warnings.
import _codecs
import _collections
import _functools
import _heapq
import _locale
import _random
import _socket
import _sre
import _stat
import _string
import _symtable
import _tracemalloc
import _weakref

# The following modules are optional and may be missing.
try:
    import _lsprof
except ImportError:
    pass

try:
    import _multibytecodec
except ImportError:
    pass

try:
    import _winreg
except ImportError:
    pass

try:
    import _winapi
except ImportError:
    pass

try:
    import _testcapi
except ImportError:
    pass

