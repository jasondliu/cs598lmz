import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CStructType = type(S)


class Test_inspect(unittest.TestCase):
    def test_isfunction(self):
        import inspect, types

        self.assertIn(inspect.isfunction(len),
                      (True, False),
                      'isfunction(len)')
        self.assertEqual(inspect.isfunction(1), False)
        self.assertEqual(inspect.isfunction('str'), False)
        self.assertEqual(inspect.isfunction(None), False)
        self.assertEqual(inspect.isfunction(len), True)

        class C(object):
            def method(self): pass
            class_m = classmethod(lambda cls: None)
            static_m = staticmethod(lambda: None)
            prop = property(lambda self: None)
        c = C()
        self.assertEqual(inspect.isfunction(c.method), False)
        self.assertEqual(inspect.isfunction(c.class_m), False)
        self.assertEqual
