import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# Modules that are optional and may not be present
_sysconfigdata = None
try:
    import _sysconfigdata
except ImportError:
    pass

_winreg = None
try:
    import _winreg
except ImportError:
    pass

_winapi = None
try:
    import _winapi
except ImportError:
    pass

# Modules that are present on Windows only
_msilib = None
try:
    import _msilib
except ImportError:
    pass

_multiprocessing = None
try:
    import _multiprocessing
except ImportError:
    pass

_overlapped = None
try:
    import _overlapped
except ImportError:
    pass

_winxptheme = None
try:
    import _winxptheme
except ImportError:
    pass

_dummy_threading = None
try:
    import _
