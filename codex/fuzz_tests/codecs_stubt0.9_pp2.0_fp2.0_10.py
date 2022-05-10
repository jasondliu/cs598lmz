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

class UnicodeEncoderTest(unittest.TestCase):

    def test_basics(self):
        html = '<html><head></head><body><h1>The Python Unicode HOWTO</h1></body></html>'
        self.assertEqual(html, html.encode('ascii').decode('ascii'))

        name = 'François Pinard'
        self.assertNotEqual(name, name.encode('ascii'))
        self.assertEqual(name, name.encode('utf-8').decode('utf-8'))

        cafe = 'café'
        self.assertNotEqual(cafe, cafe.encode('ascii'))
        self.assertEqual(cafe, cafe.encode('utf-8').decode('utf-8'))

    def test_codepoints(self):
        self.assertEqual(ord('a'), 97)
        self.assertEqual(chr(97), 'a')

        self.assertEqual(ord('é'),
