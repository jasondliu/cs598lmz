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

# Test for issue #14558
# http://bugs.python.org/issue14558
#
# This test is not complete. It only tests that the codecs module
# can be imported and that the codecs.register_error function is
# available.

def test_main():
    import codecs
    codecs.register_error("add_one_codepoint", add_one_codepoint)
    codecs.register_error("add_utf16_bytes", add_utf16_bytes)
    codecs.register_error("add_utf32_bytes", add_utf32_bytes)

if __name__ == "__main__":
    test_main()
