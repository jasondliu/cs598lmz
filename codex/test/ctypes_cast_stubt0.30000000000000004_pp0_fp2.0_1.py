import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a workaround for a ctypes bug on OS X:
# http://bugs.python.org/issue13990
import sys
if sys.platform == 'darwin':
    import _ctypes
    _ctypes.PyObj_FromPtr(id(None))

# This is a workaround for a ctypes bug on OS X:
# http://bugs.python.org/issue13990
import sys
if sys.platform == 'darwin':
    import _ctypes
    _ctypes.PyObj_FromPtr(id(None))

# This is a workaround for a ctypes bug on OS X:
# http://bugs.python.org/issue13990
import sys
if sys.platform == 'darwin':
    import _ctypes
    _ctypes.PyObj_FromPtr(id(None))

# This is a workaround for a ctypes bug on OS X:
# http://bugs.python.org/issue13990
import sys
if sys.platform == 'darwin':
    import _ctypes
