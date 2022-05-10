import _struct
# Test _struct.Struct.

class StructTest(unittest.TestCase):

    def create_binary_test(self, s):
        self.assertEqual(s.format, s.create_binary_test().format)

    def sizeof_test(self, s):
        self.assertEqual(s.format, s.create_binary_test().format)
        self.assertEqual(s.size, s.create_binary_test().size)

    def pack_test(self, s, args):
        bin = s.pack(*args)
        self.assertEqual(s.format, s.create_binary_test().format)
        self.assertEqual(s.size, len(bin))
        self.assertEqual(s.unpack(bin), args)

    def pack_into_test(self, s, args, expbuf):
        buf = array.array('c', expbuf)
        self.assertEqual(s.pack_into(buf, 0, *args), None)
        self.assertEqual(buf, array.array('c', expbuf))


