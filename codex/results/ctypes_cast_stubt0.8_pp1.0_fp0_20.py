import ctypes
ctypes.cast(42, ctypes.py_object)
_old_obj = object()
_new_obj = object()
ctypes.cast(_old_obj, ctypes.py_object) is _old_obj
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
ptr = ctypes.pythonapi.PyCapsule_GetPointer(ctypes.py_object(_new_obj), None)
ctypes.cast(ptr, ctypes.py_object) is _new_obj
ctypes.pythonapi.PyCapsule_GetName.restype = ctypes.c_char_p
ctypes.pythonapi.PyCapsule_GetName.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyCapsule_GetName(ctypes.py_object(_new_obj))


# ## 7.4.4 C types 和
