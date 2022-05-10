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
    # These tests are only relevant for UCS2 builds.
    if sys.maxunicode != 0xffff:
        return

    # Test that the codecs module is able to call back into
    # the Python codecs to fixup the errors.
    #
    # The first test checks that the codecs module is able to
    # call back into the Python codecs to fixup the errors.
    #
    # The second test checks that the codecs module is able to
    # call back into the Python codecs to fixup the errors
    # when the codecs are registered in a different module.
    #
    # The third test checks that the codecs module is able to
    # call back into the Python codecs to fixup the errors
    # when the codecs are registered in a different module
    # and the codecs are registered using a function.

    for encoding in ["utf-8", "utf-16", "utf-32"]:
        for errors in ["strict", "replace", "ignore", "add_one_codepoint", "add_utf16_
