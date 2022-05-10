import ctypes
ctypes.cast(obj, ctypes.py_object).value

# or

import ctypes
id(obj) == ctypes.cast(ctypes.py_object(obj), ctypes.c_void_p).value
</code>

