import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)  # for testing

class Int(int):
    pass

class Float(float):
    pass

class Unicode(str):
    pass

class Bytes(bytes):
    pass

class Tuple(tuple):
    pass

class List(list):
    pass

class Dict(dict):
    pass

class Set(set):
    pass

class Frozenset(frozenset):
    pass

class Obj:
    pass


class Test_get_castargs(unittest.TestCase):
    def check_basic(self, type):
        if type is float:
            value = ctypes.cast(ctypes.pointer(ctypes.c_double(1.0)),
                                ctypes.POINTER(type))
            self.assertEqual(ctypes._get_castargs(value), (1.0,))
        else:
            value = ctypes.cast(ctypes.pointer(ctypes.c_int(1)),
                                ctypes.POINTER(type))
            self.assertEqual(ctypes._
