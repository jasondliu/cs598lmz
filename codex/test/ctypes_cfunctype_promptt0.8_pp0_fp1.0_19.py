import ctypes
# Test ctypes.CFUNCTYPE 
#%cflags linux 
#%include "dynload/python_mod_support.i"

ctypes.pythonapi.PyObject_GetAttrString.restype = ctypes.py_object
ctypes.pythonapi.PyObject_GetAttrString.argtypes = [ctypes.py_object, ctypes.c_char_p]

ctypes.pythonapi.PyObject_CallMethod.restype = ctypes.py_object
ctypes.pythonapi.PyObject_CallMethod.argtypes = [ctypes.py_object, ctypes.c_char_p, ctypes.c_char_p]

ctypes.pythonapi.PyObject_CallFunction.restype = ctypes.py_object
ctypes.pythonapi.PyObject_CallFunction.argtypes = [ctypes.py_object, ctypes.c_char_p]

