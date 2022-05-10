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
    # test codecs.escape_decode()
    test_escape_decode()

    # test codecs.escape_encode()
    test_escape_encode()

    # test codecs.charmap_encode()
    test_charmap_encode()

    # test codecs.charmap_decode()
    test_charmap_decode()

    # test codecs.charmap_build()
    test_charmap_build()

    # test codecs.unicode_internal_encode()
    test_unicode_internal_encode()

    # test codecs.unicode_internal_decode()
    test_unicode_internal_decode()

    # test codecs.utf_7_encode()
    test_utf_7_encode()

    # test codecs.utf_7_decode()
    test_utf_7_decode()

    # test codecs.utf_8_encode()
    test_utf_8_encode()

    # test
