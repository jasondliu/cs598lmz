import _struct
import _thread
import _threading
import _time
import _token
import _traceback
import _types
import _warnings
import _weakref

# The _winreg module is not present on non-Windows platforms
try:
    import _winreg
except ImportError:
    pass

# The _winapi module is not present on non-Windows platforms
try:
    import _winapi
except ImportError:
    pass

# The _winxptheme module is not present on non-Windows platforms
try:
    import _winxptheme
except ImportError:
    pass

# The _xxsubinterpreters module is not present on non-Windows platforms
try:
    import _xxsubinterpreters
except ImportError:
    pass

# The _multiprocessing module is not present on non-Windows platforms
try:
    import _multiprocessing
except ImportError:
    pass

# The _overlapped module is not present on non-Windows platforms
try:
    import _overlapped
except ImportError:
    pass

