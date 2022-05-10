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

class CodecTestCase(unittest.TestCase):
    def test_decode_bom(self):
        # BOM in file, not in data
        data = b'\x00\x01\x02'
        expected = data.decode('utf-16')
        self.assertEqual(data.decode('utf-16-le'), expected)
        self.assertEqual(data.decode('utf-16-be'), expected)
        self.assertEqual(data.decode('utf-16-ex'), expected)
        self.assertEqual(data.decode('utf-16-le-ex'), expected)
        self.assertEqual(data.decode('utf-32-ex'), expected)
        self.assertEqual(data.decode('utf-32-le-ex'), expected)
        self.assertEqual(data.decode('utf-32-be-ex'), expected)

        data = b'\x00\x00\x00'
        expected = data.decode('utf-32')
        self.assertE
