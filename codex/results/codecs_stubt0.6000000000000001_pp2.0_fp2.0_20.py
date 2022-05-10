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

class TestErrors(unittest.TestCase):

    def test_xmlcharrefreplace(self):
        self.assertEqual(
                b'&#65534;&#65535;'.decode('ascii', 'xmlcharrefreplace'),
                '\ufffe\uffff'
                )
        self.assertEqual(
                b'&#65535;&#65534;'.decode('ascii', 'xmlcharrefreplace'),
                '\uffff\ufffe'
                )

    def test_backslashreplace(self):
        self.assertEqual(
                b'\xff'.decode('ascii', 'backslashreplace'),
                '\\xff'
                )
        self.assertEqual(
                b'\xff'.decode('ascii', 'replace'),
                '\ufffd'
                )
        self.assertEqual(
                b'\xff'.decode('ascii', 'ignore'),
                ''
                )

    def test_surrogatepass(self):
        self.
