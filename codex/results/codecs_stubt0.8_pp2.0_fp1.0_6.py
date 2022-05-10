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


class BOMTest(unittest.TestCase):

    def test_readbom(self):
        s = codecs.BOM_UTF8.decode('utf-8')
        self.assertEqual(s, '\ufeff')

    def test_writebom(self):
        self.assertEqual(codecs.BOM_UTF8.encode('utf-8'), b'\xef\xbb\xbf')

    def test_readbom_le(self):
        s = codecs.BOM_UTF16_LE.decode('utf-16-le')
        self.assertEqual(s, '\ufeff')

    def test_writebom_le(self):
        self.assertEqual(
            codecs.BOM_UTF16_LE.encode('utf-16-le'), b'\xff\xfe')
        self.assertEqual(codecs.BOM_UTF16_BE.encode('utf-16-be'), b'\xfe\xff')


class DecodeTest(
