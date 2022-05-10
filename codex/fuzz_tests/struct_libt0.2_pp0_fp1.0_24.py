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

_win32com = None
try:
    import _win32com
except ImportError:
    pass

_win32comloader = None
try:
    import _win32comloader
except ImportError:
    pass

_win32con = None
try:
    import _win32con
except ImportError:
    pass

_win32crypt = None
try:
    import _win32crypt
except ImportError:
    pass

