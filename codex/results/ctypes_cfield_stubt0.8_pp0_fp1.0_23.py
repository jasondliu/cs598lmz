import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    pass

class MyUnion(ctypes.Union):
    _fields_ = [('a', ctypes.c_int),
                ('b', X)]

ctypes.CFieldUnion = type(MyUnion.a)

class MyStructure(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('u', MyUnion),
                ('b', X)]

ctypes.CFieldStructure = type(MyStructure.a)

class MyPOINTER(ctypes.POINTER(ctypes.c_int)):
    pass

ctypes.CPointer = type(MyPOINTER)

class MyARRAY(ctypes.c_int * 7):
    pass

ctypes.CArray = type(MyARRAY)

ctypes.CFuncPtr = type(lambda x: True)
