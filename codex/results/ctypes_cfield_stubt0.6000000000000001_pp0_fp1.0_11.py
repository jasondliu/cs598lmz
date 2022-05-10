import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

def test_CField():
    assert isinstance(C.x, ctypes.CField)
    assert C.x.offset == 0
    assert C.x.size == ctypes.sizeof(ctypes.c_int)
    assert C.x.index == 0
    assert C.x.name == 'x'
    assert repr(C.x) == '<Field type=c_int, ofs=0>'
    assert C.x._type_ is ctypes.c_int

################################################################

if __name__ == '__main__':
    test_CField()
