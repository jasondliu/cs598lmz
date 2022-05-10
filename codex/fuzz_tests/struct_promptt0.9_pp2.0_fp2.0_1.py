import _struct
# Test _struct.Struct definition.
#
# Based on code snippet posted by Jason Orendorff in
# https://mail.python.org/pipermail/python-list/2005-September/318334.html
class StructTest(unittest.TestCase):
    def test_calcsize(self):
        self.assertEqual(_struct.calcsize("hi"), 4)

    def test_pack(self):
        self.assertEqual(_struct.pack("hi", 0xdeadbeef, 0xcafebabe),
                         b'\xef\xbe\xad\xde\xbe\xba\xfe\xca')
        self.assertRaises(_struct.error, _struct.pack, "hi", 0xffffffff, 0xff)

    def test_unpack(self):
        self.assertEqual(_struct.unpack("hi",
                                        b'\xef\xbe\xad\xde\xbe\xba\xfe\xca'),
                         (0xdeadbeef, 0xcafebabe))
        self.assertRaises(_struct
