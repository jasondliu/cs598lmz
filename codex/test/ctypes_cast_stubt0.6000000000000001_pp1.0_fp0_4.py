import ctypes
ctypes.cast(0, ctypes.py_object)
# ctypes.cast(0, ctypes.py_object).value

import sys
sys.getrefcount(None)

a = None
sys.getrefcount(None)

b = None
sys.getrefcount(None)

del a
sys.getrefcount(None)

del b
sys.getrefcount(None)

# ctypes.cast(0, ctypes.py_object).value

None is None
None is not None

None == None
None != None

