import _struct
# Test _struct.Struct
try:
    import operator
except:
    operator = None

class StructTestCase(unittest.TestCase):

    def testDefaultSize(self):
        import _struct
        self.assertEqual(4, _struct.calcsize('i'))
        self.assertEqual(4, _struct.calcsize('l'))
        self.assertEqual(8, _struct.calcsize('q'))

    def testFirstArgIsString(self):
        # SF buf 1647541
        self.assertRaises(TypeError, _struct.pack, 42, b'i', 0)
        # SF bug 1515767
        self.assertRaises(TypeError, _struct.unpack, 42, b'xxxx')

    def testVariousPackObjects(self):
        # assert that various pack objects have the expected size.
        self.assertEqual(_struct.Struct('b').size, 1)
        self.assertEqual(_struct.Struct('h').size, 2)
        self.assertEqual(_struct.Struct('i').size, 4)
