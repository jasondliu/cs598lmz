import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class TestPyGetSetDescriptor(unittest.TestCase):

    def test_c_field_subclass(self):

        class Foo(object):
            pass

        class Bar(ctypes.CField):
            pass

        class Baz(ctypes.CFieldSubclass):
            _type_ = "b"

        class Qux(object):
            # compose a CField object
            x = ctypes.c_int.in_dll(ctypes, "foo")

            # add another descriptor of the same type
            y = Bar.in_dll(ctypes, "bar")

            # add a non-CFieldSubclass descriptor
            z = Foo()

            # add a descriptor subclassing CFieldSubclass
            w = Baz.in_dll(ctypes, "baz")

        self.assertTrue(issubclass(type(Qux.x), ctypes.CField))
        self.assertTrue(issubclass(type(Qux.y), ctypes.CField))
        self.assertFalse(issubclass(type(Qux.z), c
