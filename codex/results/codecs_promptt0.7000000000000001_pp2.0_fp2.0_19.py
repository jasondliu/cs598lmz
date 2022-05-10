import codecs
# Test codecs.register_error()
def bad_encode(e):
    raise UnicodeEncodeError("bad_encode", e.object, e.start, e.end, "bad_encode")
def bad_decode(e):
    raise UnicodeDecodeError("bad_decode", e.object, e.start, e.end, "bad_decode")
def bad_replace(e):
    raise UnicodeDecodeError("bad_replace", e.object, e.start, e.end, "bad_replace")
class BadEncodeTest(unittest.TestCase):
    def test_bad_encode(self):
        self.assertRaises(UnicodeEncodeError, codecs.register_error("bad_encode", bad_encode), "1")
    def test_bad_decode(self):
        self.assertRaises(UnicodeDecodeError, codecs.register_error("bad_decode", bad_decode), "1")
    def test_bad_replace(self):
        self.assertRaises(UnicodeDecodeError, codecs.
