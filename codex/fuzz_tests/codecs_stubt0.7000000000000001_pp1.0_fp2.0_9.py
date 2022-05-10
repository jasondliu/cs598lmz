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

class TestCodecs(unittest.TestCase):
    def setUp(self):
        self.str = '\u1234\u5678\u9abc' # surrogate pairs in 32-bit builds
        self.strU = '\U00012345' # single character in 32-bit builds
        self.bstr = self.str.encode('utf-16-le')
        self.bstrU = self.strU.encode('utf-16-le')

        if sys.maxunicode > 0xffff:
            # utf-32 is a no-op in 32-bit builds and we can't decode
            # our own utf-32 encoded string
            self.bstr = self.str.encode('utf-32-be')
            self.bstrU = self.strU.encode('utf-32-be')

        self.bstr = self.bstr.replace(b'\x00', b'', 1)
        self.bstrU = self.bstrU.replace(b'\x00', b'', 1)
