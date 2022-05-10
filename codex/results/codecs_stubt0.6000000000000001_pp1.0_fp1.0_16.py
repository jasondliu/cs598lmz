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
    def test_decode_error_handling(self):
        # Test codecs.decode() handling of UnicodeDecodeErrors.
        # Issue #19449
        tests = [
            ("\xc0", "latin-1", "replace", "\ufffd"),
            ("\xc0", "latin-1", "ignore", ""),
            ("\xc0", "latin-1", "xmlcharrefreplace", "&#192;"),
            ("\xc0", "latin-1", "backslashreplace", "\\xC0"),
            ("\xc0", "latin-1", "namereplace", "\\N{LATIN CAPITAL LETTER A WITH GRAVE}"),
            ("\xc0", "latin-1", "add_one_codepoint", "a\xc0"),
            ("\xc0", "latin-1", "add_utf16_bytes", "a\xc0"),
            ("\xc0", "latin-1", "add_utf
