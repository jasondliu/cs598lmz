import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)


class EncodingTest(unittest.TestCase):

    def tearDown(self):
        # if we don't do this, the pymalloc allocator keeps a reference
        # to the unicode string.
        for attr in dir(self):
            if attr.startswith("uni") and not attr.endswith("_embed"):
                setattr(self, attr, None)
            if attr.startswith("byt"):
                setattr(self, attr, None)

    def test_utf8(self):
        self.encode_test('utf-8')

    def test_latin1(self):
        self.encode_test('latin-1')

    def test_ascii(self):
        self.encode_test('ascii')

    def test_bz2_encode(self):
        tt = [
            ('hello', b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00
