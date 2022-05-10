import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)


class C():
    def __init__(self):
        self.f = ctypes.c_int()

ctypes.CData = type(C().f)


class Foo(object):
    pass

def pickle_CData(obj):
    return unpickle_CData, (ctypes.c_char_p(obj).value,)

def unpickle_CData(data):
    return pickle.loads(data)

def pickle_CField(obj):
    return unpickle_CField, (ctypes.c_char_p(obj).value,)

def unpickle_CField(data):
    return pickle.loads(data)

class Test(unittest.TestCase):
    def test_cdata(self):
        s = 'hello world'
        buf = ctypes.create_string_buffer(s)
        self.assertEqual(buf.value, s)

        p = pickle.dumps(buf)
        buf2 = pickle.loads(p)
        self.assertEqual(buf2.
