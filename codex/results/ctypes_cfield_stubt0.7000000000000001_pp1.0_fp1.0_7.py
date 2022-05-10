import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

del S

def check_type(cls):
    return cls is ctypes.CField

class Int(ctypes.c_int):
    pass

class Test(unittest.TestCase):
    def test_wrong_fields(self):
        # Test that an invalid field spec generates a ValueError
        for fields in (17, object(), object, (), (1, 2), (1, 2), ("x",),
                       ("x", 1, 2), ("x", "y", "z"), ("y", "x", "x"),
                       ("x", "x", "x"), ("_f_",), ("_f_", "y"), ("x", "_f_")):
            self.assertRaises(ValueError, ctypes.Structure, "S", fields)
            self.assertRaises(ValueError, ctypes.Union, "U", fields)

        # Test that _fields_ cannot be overridden
        self.assertRaises(AttributeError, setattr, ctypes.Structure, "_fields_", None)
        self.assertRaises(AttributeError,
