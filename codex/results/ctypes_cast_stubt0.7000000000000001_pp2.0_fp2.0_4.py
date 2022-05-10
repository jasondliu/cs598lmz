import ctypes
ctypes.cast(123, ctypes.py_object)

#from ctypes import pythonapi, py_object
#pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
#pythonapi.PyCObject_AsVoidPtr.argtypes = [py_object]
#pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(123))

#from ctypes import *
#c_void_p.in_dll(pythonapi, "PyCObject_Type").value

#from ctypes import *
#c_void_p.from_address(id(123)).value
