import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_type_and_offset(self):
        class Foo(ctypes.Structure):
            _fields_ = [('a', ctypes.c_short, 2),
                        ('b', ctypes.c_short, 4),
                        ('c', ctypes.c_short, 10),
                        ('d', ctypes.c_short, 1)]
        self.assertEqual(ctypes.sizeof(Foo), 4)
        self.assertEqual(Foo.a.offset, 0)
        self.assertEqual(Foo.b.offset, 0)
        self.assertEqual(Foo.c.offset, 2)
        self.assertEqual(Foo.d.offset, 2)
        self.assertEqual(Foo.a.size, 2)
        self.assertEqual(Foo.b.size, 4)
        self.assertEqual(Foo.c.size, 10)
        self.assertEqual(Foo.d.size, 1)

    def
