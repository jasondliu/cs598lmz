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
    # test the codecs module
    from test import test_codecs
    test_codecs.test_main()

    # test the encodings package
    from test import test_encodings
    test_encodings.test_main()

    # test the encodings.aliases module
    from test import test_aliases
    test_aliases.test_main()

    # test the encodings.mbcs module
    from test import test_mbcs
    test_mbcs.test_main()

    # test the encodings.utf_8 module
    from test import test_utf_8
    test_utf_8.test_main()

    # test the encodings.utf_16 module
    from test import test_utf_16
    test_utf_16.test_main()

    # test the encodings.utf_32 module
    from test import test_utf_32
    test_utf_32.test_main()

    # test the encodings.iso2022 module
    from test import
