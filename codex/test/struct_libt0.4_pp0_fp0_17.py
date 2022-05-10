import _struct
import _sys
import _thread
import _time
import _traceback
import _types
import _unittest
import _warnings
import _weakref
import _xxsubinterpreters

# Modules that are optional in CPython but should always be available in PyPy
import _codecs
import _collections
import _io
import _multibytecodec
import _random
import _socket
import _ssl
import _string
import _struct
import _symtable
import _weakref

# Modules that are only available on some platforms
try:
    import _curses
except ImportError:
    pass

try:
    import _curses_panel
except ImportError:
    pass

try:
    import _hashlib
except ImportError:
    pass

try:
    import _json
except ImportError:
    pass

try:
    import _lsprof
except ImportError:
    pass

try:
    import _multiprocessing
except ImportError:
    pass

