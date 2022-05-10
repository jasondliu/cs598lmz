import _struct
import _thread
import _threading
import _time
import _token
import _traceback
import _types
import _warnings
import _weakref

# Modules that are optional and may not be present
# (e.g. _elementtree is only present if the system has a C
# implementation of the expat XML parser).

try:
    import _elementtree
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
    import _multiprocessing
except ImportError:
    pass

try:
    import _sqlite3
except ImportError:
    pass

try:
    import _ssl
except ImportError:
    pass

try:
    import _tkinter
except ImportError:
    pass

try:
    import _uuid
except ImportError:
    pass

try:
    import _winreg
except ImportError:
    pass

