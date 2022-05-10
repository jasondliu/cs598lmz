import ctypes
ctypes.cast(0, ctypes.py_object)

#%%
import ctypes
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]

#%%
import ctypes
ctypes.pythonapi.PyCapsule_New.restype = ctypes.py_object
ctypes.pythonapi.PyCapsule_New.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.py_object]

#%%
import ctypes
ctypes.pythonapi.PyCapsule_IsValid.restype = ctypes.c_int
ctypes.pythonapi.PyCapsule_IsValid.argtypes = [ctypes.py_object, ctypes.c_char_p]

#%%
import ctypes
ctypes.pythonapi.PyCapsule_GetName.restype = ctypes.c_char_p
