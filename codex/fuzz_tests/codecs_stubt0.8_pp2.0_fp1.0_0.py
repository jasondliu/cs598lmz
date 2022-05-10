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

class UnicodeDecodeUnicode:
    errors = None
    
    def __init__(self):
        self.input = None
        self.instance = None

    def setUp(self):
        self.input = None
        self.instance = None

    def test_decoding_empty(self):
        self.input = b''
        self.instance = codecs.getincrementaldecoder('utf-16')()
        output = self.instance.decode(self.input)
        self.assertEqual(output, '')
        self.assertEqual(self.instance.decode(b'', True), '')

    def test_decoding_partial(self):
        self.input = b'\xff\xff'
        self.instance = codecs.getincrementaldecoder('utf-16')(self.errors)
        output = self.instance.decode(self.input)
        self.assertEqual(output, '\ufffd\ufffd')
        self.assertEqual(self.instance.decode(b'', True),
