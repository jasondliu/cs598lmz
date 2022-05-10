import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue15881#msg170215
import sys
if sys.version_info[0] == 2:
    import thread
else:
    import _thread as thread

# This is a workaround for http://bugs.python.org/issue2320
try:
    import readline
except ImportError:
    pass

# This is a workaround for http://bugs.python.org/issue17636
try:
    import winreg
except ImportError:
    pass

# This is a workaround for http://bugs.python.org/issue2320
try:
    import winreg
except ImportError:
    pass

# This is a workaround for http://bugs.python.org/issue17636
try:
    import winreg
except ImportError:
    pass

# This is a workaround for http://bugs.python.org/issue17636
try:
    import winreg
except ImportError:
    pass

# This is
