import ctypes
ctypes.cast(1, ctypes.py_object).value

# or

import ctypes
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
ctypes.pythonapi.PyCapsule_GetPointer(ctypes.py_object(1), None)
</code>

