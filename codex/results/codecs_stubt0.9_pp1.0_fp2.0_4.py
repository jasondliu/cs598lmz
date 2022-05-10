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

class TestBaseUTF(unittest.TestCase):
    encoding = None  # To be overridden.

    def test_decode(self):
        equal = self.assertEqual
        decode = codecs.getdecoder(self.encoding)

        # Sanity checks to make sure we're actually testing what we think we're
        # testing.
        equal(decode(b'\xff', "replace")[0], u'\ufffd')
        equal(decode(b'\xff', "ignore")[0], u'')
        equal(decode(b'\xff', "strict")[1], 1)
        equal(decode(b'\x00\xff', "strict")[1], 2)
        equal(decode(b'\xff', "add_one_codepoint")[0], u'a')
        equal(decode(b'\xff', "add_utf16_bytes")[0], u'ab')
        equal(decode(b'\xff', "add_utf32_bytes")[0], u'ab
