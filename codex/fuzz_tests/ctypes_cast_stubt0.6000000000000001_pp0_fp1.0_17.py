import ctypes
ctypes.cast(0, ctypes.py_object)

# SEGV

#import ctypes
#ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
#ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
#ctypes.pythonapi.PyCObject_AsVoidPtr(None)

# SEGV

#import ctypes
#ctypes.pythonapi.PyCObject_FromVoidPtr.restype = ctypes.py_object
#ctypes.pythonapi.PyCObject_FromVoidPtr.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
#ctypes.pythonapi.PyCObject_FromVoidPtr(None, None)

# SEGV

#import ctypes
#ctypes.pythonapi.PyCObject_Import.restype = ctypes.py_object
#ctypes.pythonapi.PyCObject_Import.argtypes = [ctypes.c_char_p
