import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# or
import sys
sys.getrefcount(x)

# or
x is y
</code>

