import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = ctypes.c_int(100)

ctypes.CObject = type(C().x)


def test_memory_view():
    for tp in [b't', 'B', 'b', 'c', 'u', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
        mv = memoryview(bytearray(b'abcde'))
        a = array.array(tp, mv)
        b = a.tobytes()
        assert b == mv.tobytes()
        assert a.tolist() == list(mv.cast(tp))


def test_from_buffer():
    b = bytearray(b'abcde')
    mv = memoryview(b)
    a = array.array('b', mv)
    assert a.tolist() == list(mv.cast('b'))

def test_from_buffer_
