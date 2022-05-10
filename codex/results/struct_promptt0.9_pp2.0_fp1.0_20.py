import _struct
# Test _struct.Struct.size

# Ensure valid
class Test(unittest.TestCase):
    def testSize(self):
        s = _struct.Struct("=i")
        self.assertEqual(s.size, 4)
        s = _struct.Struct("=01234x")
        self.assertEqual(s.size, 1234)

    def testBuffer(self):
        s = _struct.Struct("=i")
        self.assertEqual(s.size, 4)
        b = buffer(s.pack(32767))
        self.assertEqual(b[:], '\xff\xff\xff\x7f')

    def testRepr(self):
        s = _struct.Struct("=i")
        self.assert_(repr(s).startswith('<struct _struct.Struct object at 0x'))
        self.assertIn('format:=i', repr(s))

# Uncomment these to get test cases for bad formats.
##    def testBadFormat(self):
##        struct.Struct("=a")
##        struct.Struct
