import ctypes
# Test ctypes.CFUNCTYPE on a function with a structure parameter.
class Test(unittest.TestCase):
    def test(self):
        import _ctypes
        class struct_tag(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]
        CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(struct_tag),
                                   ctypes.POINTER(struct_tag))
        self.assertEqual(CMPFUNC.__doc__, 'int(*)(struct_tag *, struct_tag *)')
        self.assertIsInstance(CMPFUNC, _ctypes._CFuncPtr)
        self.assertIs(CMPFUNC.restype, ctypes.c_int)
        self.assertEqual(CMPFUNC.argtypes, (ctypes.POINTER(struct_tag),
                                            ctypes.POINTER(struct_tag)))
        self.assertEqual(CMPFUNC.errcheck, None)
        self.
