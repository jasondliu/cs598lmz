import ctypes
# Test ctypes.CField

class basic_test(ctypes.Structure):
    _fields_ = [("b", ctypes.c_byte),
                ("s", ctypes.c_short),
                ("i", ctypes.c_int),
                ("l", ctypes.c_long)]

class CField_Test(unittest.TestCase):
    # XXX Should test alignment too...
    def test_c_byte(self):
        self.failUnlessEqual(basic_test.b.offset, 0)
        self.failUnlessEqual(basic_test.b.size, 1)

    def test_c_short(self):
        self.failUnlessEqual(basic_test.s.offset, 2)
        self.failUnlessEqual(basic_test.s.size, 2)

    def test_c_int(self):
        self.failUnlessEqual(basic_test.i.offset, 4)
        self.failUnlessEqual(basic_test.i.size, 4)

    def test_c_long(self):
        self.failUnlessEqual
