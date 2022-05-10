import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class B(S):
    _fields_ = [('y', ctypes.c_int)]

class C(A):
    _fields_ = [('y', ctypes.c_int)]

import sys

if sys.version_info > (3,):
    long = int

class Test(unittest.TestCase):
    def test_CField(self):
        self.assertEqual(S.x, S.x)
        self.assertEqual(S.x, B.x)
        self.assertEqual(S.x, C.x)
        self.assertNotEqual(S.x, B.y)
        self.assertNotEqual(S.x, C.y)

        self.assertEqual(S.x, ctypes.CField(S, 'x'))

        self.assertEqual(S.x.name, 'x')
        self.assertEqual(S.x.
