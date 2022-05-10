import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# Modules that are optional and may not be present
_winreg = None
try:
    import _winreg
except ImportError:
    pass

_win32api = None
try:
    import _win32api
except ImportError:
    pass

_win32clipboard = None
try:
    import _win32clipboard
except ImportError:
    pass

_win32con = None
try:
    import _win32con
except ImportError:
    pass

_win32cred = None
try:
    import _win32cred
except ImportError:
    pass

_win32evtlog = None
try:
    import _win32evtlog
except ImportError:
    pass

_win32evtlogutil = None
try:
    import _win32evtlogutil
except ImportError:
    pass

_win32file = None
try:
    import _win32
