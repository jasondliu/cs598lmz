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
    test_unicode_internal_encode()
    test_unicode_encode()
    test_str_decode()
    test_unicode_decode()
    test_unicode_internal_decode()
    test_escape_decode()
    test_escape_encode()
    test_iso2022_encode()
    test_iso2022_decode()
    test_readbuffer_encode()
    test_readbuffer_decode()
    test_bug_793791()
    test_bug_449964()
    test_bug_1139()
    test_bug_1139()
    test_bug_1139()
    test_surrogates()
    test_malformed()
    test_utf8_decode()
    test_utf8_encode()
    test_lone_surrogates()
    test_bug_817234()
    test_bug_817234()
    test_bug_817234()
    test_bug_817234()
   
