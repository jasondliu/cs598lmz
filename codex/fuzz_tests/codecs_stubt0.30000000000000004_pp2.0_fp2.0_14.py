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

class TestUnicode(unittest.TestCase):

    def test_decode_error_handling(self):
        # Test Unicode decode error handling.
        #
        #   - 'strict' mode should raise a ValueError
        #   - 'replace' mode should replace the unencodable character
        #     with a '?'
        #   - 'ignore' mode should ignore the unencodable character
        #   - 'backslashreplace' should replace with backslashed escape
        #   - 'xmlcharrefreplace' should replace with XML character reference
        #   - 'add_one_codepoint' should replace with a single codepoint
        #   - 'add_utf16_bytes' should replace with two UTF-16 bytes
        #   - 'add_utf32_bytes' should replace with four UTF-32 bytes
        #
        # Note that 'add_one_codepoint', 'add_utf16_bytes' and
        # 'add_utf32_bytes' are registered error handlers.
        #
        # XXX more tests needed
        tests = [
