import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CData = type(S())

_CDATA_IS_C_DATA = issubclass(ctypes.CData, ctypes.c_ubyte)

@njit
def array_cdata_is_c_data():
    return _CDATA_IS_C_DATA

if __name__ == '__main__':
    print(array_cdata_is_c_data())
