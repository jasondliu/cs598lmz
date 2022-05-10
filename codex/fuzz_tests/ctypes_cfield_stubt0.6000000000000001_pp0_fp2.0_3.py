import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert type(S.x) is ctypes.CField

if __name__ == '__main__':
    test_cfield()
