import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

ctypes.Union = ctypes.Union
ctypes.Struct = ctypes.Struct
ctypes.CStructUnion = ctypes.CStructUnion 
ctypes.CStruct = ctypes.CStruct 

if __name__ == '__main__':
    pass
