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

class TestBrokenData:
    """
    When trying to decode broken data, a unicode_error should be thrown
    from the PyUnicode_(En|De)code_* functions.
    """
    @pytest.mark.parametrize("error_handler", ["ignore", "replace", "xmlcharrefreplace", "backslashreplace", "namereplace"])
    @pytest.mark.parametrize("input_bytes,expected", [
        # The input bytes are randomly broken in one of the first 127 codes
        (codecs.BOM_UTF8 + b"\xf0" + b"abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcab", "?"),
        (codecs.BOM_LE + b"\xff" + b"abcabcabcabcabcabcabcabcabcabcabcabc
