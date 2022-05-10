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

    def tearDown(self):
        try:
            del sys.setdefaultencoding
        except AttributeError:
            pass

    def test_lone_surrogates(self):
        # Issue #10983: Lone surrogates in UTF-8 and UTF-16 input should be
        # converted to the unicode replacement char, not cause an error.
        self.assertEqual(u'\udcff',
                         unicode(b'\xed\xb3\xbf', 'utf-8', 'replace'))
        self.assertEqual(u'\udcff',
                         unicode(b'\xed\xb3\xbf', 'utf-16', 'replace'))
        self.assertEqual(u'\udcff',
                         unicode(b'\x00\xed\x00\xb3\x00\xbf', 'utf-16', 'replace'))

    def test_strict_errors(self):
        # Issue #11649: strict error handlers should
