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

    def check_encode_decode(self, encoding, data):
        encoded = data.encode(encoding)
        decoded = encoded.decode(encoding)
        self.assertEqual(data, decoded)
        self.assertEqual(type(data), type(decoded))

    def test_utf8(self):
        data = 'hello world'
        self.check_encode_decode('utf-8', data)

        data = chr(0) + chr(255)
        self.check_encode_decode('utf-8', data)

        data = chr(1) + chr(1024)
        self.check_encode_decode('utf-8', data)

        data = chr(0) + chr(65535)
        self.check_encode_decode('utf-8', data)

        data = chr(0) + chr(65536)
        try:
            encoded = data.encode('utf-8
