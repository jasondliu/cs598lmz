import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldPointer = type(S._fields_[0][1])

# ctypes.pointer(S)(42)
# S.x.__get__(None, S)()
# S.x.__get__(S(42), S)
# S.x.__set__(S(42), 43)
# S.x.__delete__(S(42))

# ctypes.py_object(None)
# ctypes.py_object(42)
# ctypes.py_object(Ellipsis)
# ctypes.py_object(TypeError)
# ctypes.py_object(TypeError())
# ctypes.py_object(ctypes.CFuncPtr(None))
# ctypes.py_object(ctypes.CField(None))
# ctypes.py_object(ctypes.CFieldPointer(None))

# ctypes.pythonapi._Py_NoneStruct
# ctypes.pythonapi.Py_True
# ctypes.pythonapi.Py_False
# ctypes.pythonapi.Py_Ellipsis
