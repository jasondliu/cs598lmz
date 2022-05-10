import ctypes
ctypes.cast(0, ctypes.py_object)

# import ctypes
# ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
# ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]

# import numpy as np
# ctypes.pythonapi.PyArray_SimpleNewFromData.restype = ctypes.py_object
# ctypes.pythonapi.PyArray_SimpleNewFromData.argtypes = [ctypes.c_int,
#                                                        ctypes.POINTER(ctypes.c_int),
#                                                        ctypes.c_void_p]
# ctypes.pythonapi.PyArray_SimpleNewFromData(2, np.ones(5, dtype=np.int32).shape,
#                                            ctypes.pythonapi.PyCObject_AsVoidPtr(id(np.ones(5, dtype=np.int32).data)))

# ctypes.pythonapi.PyCObject_AsVoidPtr.restype
