import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class Test(unittest.TestCase):
    def test_logical_xor(self):
        ctypes.c_int.in_dll(ctypes.pythonapi, 'PyExc_StopIteration')
        self.assertRaises(AttributeError, ctypes.c_int.in_dll,
                          ctypes.pythonapi, 'PyExc_SystemError')
        self.assertRaises(AttributeError, ctypes.c_int.in_dll,
                          ctypes.pythonapi, 'not_there')
        # None is OK, doesn't raise.
        ctypes.c_int.in_dll(None, 'PyExc_StopIteration')

    def test_from_address(self):
        ctypes.c_int.from_address(id(S2.y))

    def test_bit_length(self):
        self.assertRaises(AttributeError, c
