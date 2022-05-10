import ctypes
ctypes.cast(0, ctypes.py_object)
try:
    ctypes.cast(0, ctypes.py_objects)
except TypeError:
    print("SKIP")
    raise SystemExit

# float_info
import sys
if 'py_object' in sys.float_info.__dict__:
    print("SKIP")
    raise SystemExit

# id(None) -> 0
print(id(None) == 0)
