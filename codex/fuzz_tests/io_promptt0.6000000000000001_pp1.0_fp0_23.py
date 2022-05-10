import io
# Test io.RawIOBase
class SubclassWithRawIO(io.RawIOBase):
    def readinto(self, buffer):
        return 0

class TestRawIOBase(unittest.TestCase):
    def test_io_base_attributes(self):
        f = SubclassWithRawIO()
        self.assertEqual(f.mode, 'rb', "should have a default mode")
        f.mode = 'wb'
        self.assertEqual(f.mode, 'wb', "mode should be settable")
        self.assertRaises(AttributeError, delattr, f, 'mode')
        self.assertRaises(AttributeError, setattr, f, 'mode', 'r')
        try:
            f.name
        except AttributeError:
            pass
        else:
            self.fail('should raise AttributeError')
        f.name = 'test'
        self.assertEqual(f.name, 'test')
        del f.name
        try:
            f.name
        except AttributeError:
            pass
        else:
            self.fail('
