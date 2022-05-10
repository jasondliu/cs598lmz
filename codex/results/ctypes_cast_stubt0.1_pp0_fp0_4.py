import ctypes
ctypes.cast(0, ctypes.py_object)

# %%
import ctypes
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]

# %%
import ctypes
ctypes.pythonapi.PyCapsule_GetName.restype = ctypes.c_char_p
ctypes.pythonapi.PyCapsule_GetName.argtypes = [ctypes.py_object]

# %%
import ctypes
ctypes.pythonapi.PyCapsule_GetDestructor.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetDestructor.argtypes = [ctypes.py_object]

# %%
import ctypes
ctypes.pythonapi.PyCapsule_GetContext.restype = ctypes.py_object
ctypes.pythonapi.PyCapsule_GetContext.argtypes = [
