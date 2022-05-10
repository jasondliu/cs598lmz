import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
CFieldPointer = ctypes.POINTER(ctypes.CField)

ptr = ctypes.pointer(S.x) # This is a CFieldPointer
#print(type(ptr))

if __name__ == '__main__':
    import test_my_extension
