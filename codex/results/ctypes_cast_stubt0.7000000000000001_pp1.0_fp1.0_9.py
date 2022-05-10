import ctypes
ctypes.cast(p, ctypes.py_object).value = a

import sys
print sys.getrefcount(a) # prints out 2
</code>

