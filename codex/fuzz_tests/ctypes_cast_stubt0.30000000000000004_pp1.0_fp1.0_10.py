import ctypes
ctypes.cast(0, ctypes.py_object)

# %%
import ctypes
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]

# %%
import ctypes
ctypes.pythonapi.PyCapsule_GetField.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetField.argtypes = [ctypes.py_object, ctypes.c_char_p]

# %%
import ctypes
ctypes.pythonapi.PyCapsule_SetField.restype = ctypes.c_int
ctypes.pythonapi.PyCapsule_SetField.argtypes = [ctypes.py_object, ctypes.c_char_p, ctypes.c_void_p]

# %%
import ctypes
ctypes.pythonapi.PyCapsule_SetDestructor.restype = ctypes
