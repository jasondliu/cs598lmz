import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(BaseTestChecker):

    def test_attributes(self):
        self.assertIsInstance(ctypes.CFuncPtr.argtypes, property)
        self.assertIsInstance(ctypes.CFuncPtr.errcheck, property)
        self.assertIsInstance(ctypes.CFuncPtr.restype, property)

    def test_c_object_p_invalid_error(self):
        if ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_int):
            type = ctypes.c_int
        else:
            type = ctypes.c_long
        self.assertEqual(ctypes.cast(None, ctypes.c_void_p).value, 0)
        with self.assertRaises((IOError, OSError)) as cm:
            ctypes.cast(0, type).value
        with patch('ctypes.test.test_cfunctype.open') as open:
            open.side_effect = [IOError, OSError, None]
