import ctypes
# Test ctypes.CFUNCTYPE
pyobj = ctypes.pythonapi.PyCapsule_New(ctypes.py_object(1), 0, ctypes.c_void_p())
if pyobj:
    ctypes.pythonapi.PyCapsule_GetPointer(pyobj, 0)
    if pyobj:
        ctypes.pythonapi.PyCapsule_IsValid(pyobj, 0)
        if pyobj:
            ctypes.pythonapi.PyCapsule_SetDestructor(pyobj, ctypes.c_void_p())
            ctypes.pythonapi.PyCapsule_Destruct(pyobj)
