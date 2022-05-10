import ctypes
ctypes.cast(addr, ctypes.py_object).value

# ctypes
import ctypes
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyCObject_AsVoidPtr(addr)

# ctypes
import ctypes
ctypes.pythonapi.PyCObject_FromVoidPtr.restype = ctypes.py_object
ctypes.pythonapi.PyCObject_FromVoidPtr.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
ctypes.pythonapi.PyCObject_FromVoidPtr(addr, None)

# ctypes
import ctypes
ctypes.pythonapi.PyCObject_Import.restype = ctypes.py_object
ctypes.pythonapi.PyCObject_Import.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
ctypes.pythonapi
