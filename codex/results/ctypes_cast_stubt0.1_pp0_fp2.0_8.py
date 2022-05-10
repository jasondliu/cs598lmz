import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# or

import sys
sys.getrefcount(obj)
</code>

