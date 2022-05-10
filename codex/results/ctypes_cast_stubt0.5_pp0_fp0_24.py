import ctypes
ctypes.cast(0, ctypes.py_object)

#s = ctypes.cast(0, ctypes.py_object)
#s.value
#s.value = 'howdy'
#s.value

#ctypes.pythonapi.PyCObject_FromVoidPtr.restype = ctypes.py_object
#ctypes.pythonapi.PyCObject_FromVoidPtr.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
#ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
#ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]

#def ref(obj):
#    return ctypes.pythonapi.PyCObject_FromVoidPtr(
#        id(obj), lambda x: None)

#def deref(ref):
#    return ctypes.pythonapi.PyCObject_AsVoidPtr(ref)

#ref('howdy')
#deref(ref('
