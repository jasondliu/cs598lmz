import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_instance():
    # Test for SF bug #1544997
    assert isinstance(S.x, ctypes.CField)

if __name__ == "__main__":
    test_cfield_instance()
