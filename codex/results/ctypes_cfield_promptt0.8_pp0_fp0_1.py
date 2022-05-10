import ctypes
# Test ctypes.CField
#
# This tests whether, in class A, the int and float fields
# are in the right order, and whether they are of the right size,
# and whether they are properly aligned.

class A(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('f1', ctypes.c_int, 4),
                ('f2', ctypes.c_float, 4),
                ('f3', ctypes.c_int, 4)]
    def __repr__(self):
        return self.__class__

if __name__ == '__main__':
    import unittest

    class CFieldTestCase(unittest.TestCase):
        def test_fields(self):
            self.assertTrue(hasattr(ctypes.c_int, '__ctype_be__'))
            self.assertTrue(hasattr(A, 'f1'))
            self.assertTrue(hasattr(A, 'f2'))
            self.assertTrue(hasattr(A, 'f3'))
            a = A()
           
