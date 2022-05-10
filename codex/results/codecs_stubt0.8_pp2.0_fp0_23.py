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

class TestMbcs(unittest.TestCase):
    # The mapping files for the different code pages are generated
    # by scripts/make_cpXXXXXX.py in the PC/VS7.1 directory.

    def test_code_page_949(self):
        self.assertEqual('abc', 'abc'.encode('mbcs'))
        self.assertEqual('abc', b'abc'.decode('mbcs'))

        a = chr(0xac00) + chr(0xac01)
        self.assertEqual(a.encode('mbcs'), b'\xb0\xa1\xb0\xa2')
        self.assertEqual(a, '\xb0\xa1\xb0\xa2'.decode('mbcs'))
        self.assertEqual(a.encode('mbcs', 'replace'), b'??')
        self.assertEqual(a.encode('mbcs', 'ignore'), b'')

        self.assertEqual(a.encode('mbcs', 'add_one_cod
