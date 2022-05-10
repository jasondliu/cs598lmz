import ctypes
ctypes.cast(0, ctypes.py_object)

class PythonAPISubclass(ctypes.pythonapi): 
    _fields_ = [('PyLong_FromLong', ctypes.PYFUNCTYPE(ctypes.py_object, ctypes.c_long)),]

# get the actual function pointer, so that we can call it directly
