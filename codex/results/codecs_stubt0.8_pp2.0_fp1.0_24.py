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

class TestRegistry:

    def test_error_handler_registration(self):
        with pytest.raises(LookupError):
            codecs.lookup_error("undefined error handler")
        with pytest.raises(LookupError):
            codecs.lookup_error("")
        with pytest.raises(LookupError):
            codecs.lookup_error(" ")
        with pytest.raises(LookupError):
            codecs.lookup_error("\u0000")
        with pytest.raises(LookupError):
            codecs.lookup_error("\U00020000")
        with pytest.raises(LookupError):
            codecs.lookup_error("U0001F4A9")
        with pytest.raises(LookupError):
            codecs.lookup_error("\u007f")

        assert codecs.lookup_error("replace") is codecs.replace_errors
        assert codecs.lookup_error("ignore") is codecs.ignore_errors
        assert
