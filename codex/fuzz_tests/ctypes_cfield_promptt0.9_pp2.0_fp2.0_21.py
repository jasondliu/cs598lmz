import ctypes
# Test ctypes.CField and ctypes._CDatafields.
import _ctypes_test

import unittest


class CField(unittest.TestCase):
    def testCField(self):
        # check the python attribute accessor of a basic ctypes data field
        class A(ctypes.Structure):
            _fields_ = [("foo", ctypes.c_int)]

        a = A()
        a.foo = 50
        self.assertEqual(a.foo, 50)

        # check the cdata data field gets
        self.assertEqual(ctypes.cdata(a).foo, 50)
        self.assertEqual(a.__getattr__("foo"), 50)

        # check the cdata data field sets
        ctypes.cdata(a).foo = 150

        self.assertEqual(a.foo, 150)
        self.assertEqual(ctypes.cdata(a).foo, 150)
        self.assertEqual(a.__getattr__("foo"), 150)

    def testTPField(self):
        # check the python attribute access
