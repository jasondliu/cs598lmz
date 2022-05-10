import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    CField = type(S.x)

class D(object):
    CField = type(S.x)
    def __getattr__(self, attr):
        return attr

class E(D):
    pass
d = D()
e = E()

#----------------------------------------------------------------------

import unittest


class TestCtypes(unittest.TestCase):
    def test_issue_3879(self):
        self.assertEqual(ctypes.CField, type(S.x))

    def test_issue_3880(self):
        self.assertEqual(C.CField, type(S.x))

    def test_issue_3881(self):
        self.assertEqual(D.CField, type(S.x))
        self.assertEqual(d.CField, 'CField')
        self.assertEqual(e.CField, 'CField')
        self.assertEqual(e.__dict__, {})
        self.assertEqual(e.__class
