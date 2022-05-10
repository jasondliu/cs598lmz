import ctypes
# Test ctypes.CField(), a new container used for instance attributes
import platform
import unittest

class XXXTestCase(unittest.TestCase):
    def test_new_class(self):
        # Cannot create an new class, should raise AttributeError

        with self.assertRaises(TypeError):
            class X(ctypes.CField):
                pass

class FieldTestCase(unittest.TestCase):
    def test_class_attributes(self):

        class _Test(ctypes._CField):
            _type_ = ctypes.c_int

            def _offset(self):
                return ctypes.addressof(self) - ctypes.addressof(self._owner)

            def _set_owner(self, owner):
                self._owner = owner

        class Test(ctypes.Structure):
            _fields_ = [("foo", _Test)]

        class Test1(ctypes.Structure):
            x = Test()

        self.assertEqual(Test1.x.offset, ctypes.addressof(Test1.x.foo) - ctypes
