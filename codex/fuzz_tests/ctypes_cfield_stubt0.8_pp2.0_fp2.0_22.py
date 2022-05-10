import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_CField():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.__name__ == "x"

if __name__ == "__main__":
    test_CField()
