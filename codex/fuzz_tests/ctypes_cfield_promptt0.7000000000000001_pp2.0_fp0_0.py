import ctypes
# Test ctypes.CField.

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

def test_cfields(testcase):
    a, b, c = X(), Y(), Z()
    a.a = b"12"
    a.b = b"34"
    b.x = a
    b.y = b"56"
    c.y = b
    c.z = b"78"
    testcase.assertEqual(c.y.x.a, 0x313233)
    testcase.assertEqual(c.y.x.b, 0x343536)
    testcase.assertEqual(c.y.y, 0x373839)
