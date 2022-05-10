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

def test_main():
    sample_data = "12345"
    from test.test_support import import_module
    unicodedata = import_module('unicodedata')

    def check(dummy, input, expected, errors="strict"):
        d = codecs.getincrementaldecoder("utf-8")(errors)
        result = d.decode(input)
        if result != expected:
            print("input:", repr(input))
            print("result:", repr(result))
            print("expected:", repr(expected))
            raise AssertionError("unexpected decoder output")
        if d.decode("", True) != "":
            raise AssertionError("decoder.decode(\"\", True) != \"\"")
        if d.decode("", False) != "":
            raise AssertionError("decoder.decode(\"\", False) != \"\"")
        expectedstate = None
        if errors in ("replace", "add_one_codepoint"):
            # state at end of input with one byte missing
