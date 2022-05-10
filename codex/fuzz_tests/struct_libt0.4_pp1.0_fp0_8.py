import _struct
import _sys
import _time
import _thread
import _threading
import _weakref
import _winreg
import _winsound
import _xml
import _zipfile
import _zlib

# These modules are implemented as dynamically loaded extensions,
# so they're not in _setup.py.
import _ctypes
import _hashlib
import _multiprocessing
import _ssl
import _tkinter

# These modules are not built by default, but can be if the user requests it.
# They are not imported here.
import _testcapi
import _bz2
import _decimal
import _elementtree
import _gdbm
import _lzma
import _msi
import _sqlite3
import _tkinter_test
import _uuid
import _winapi

# These modules are not available on all platforms
try:
    import _curses
except ImportError:
    pass

try:
    import _curses_panel
except ImportError:
    pass

try:
    import _testconsole
except ImportError:
    pass

