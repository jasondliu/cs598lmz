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

class UTF7Test(unittest.TestCase):
    encoded = ('ABC \xd1', '+ACA-CC-')
    encoding = 'utf-7'
    decimal = (65, 66, 67, 32, 7697,)
    named = ('A', 'B', 'C', ' ', '\x97',)
    not_named = ('`', '"', '\'', '-', '+', '&', '\x08')

    def test_decode(self):
        self.decode(self.encoded, self.decimal)

    def test_encode(self):
        self.encode(self.decimal, self.named)

    def test_encoded(self):
        s = '+ACA-CC-\n'.strip('\n')
        self.encode(s, self.named)
        self.decode(s, self.decimal)

    def test_invalid(self):
        codec = codecs.getencoder(self.encoding)

        for chars in self.not_named:
            for
