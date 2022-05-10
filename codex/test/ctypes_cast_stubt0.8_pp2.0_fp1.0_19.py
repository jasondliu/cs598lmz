import ctypes
ctypes.cast(1, ctypes.py_object)

import sys
sys.getrefcount(1)

ctypes.cast(1, ctypes.py_object)

sys.getrefcount(1)

#MemoryView

s = b'Hello World'

mv = memoryview(s)

#Operation on mv and s is identical

