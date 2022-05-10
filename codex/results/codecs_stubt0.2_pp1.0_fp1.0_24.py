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
    # Test UTF-8
    for i in range(0xD800, 0xE000):
        try:
            s = chr(i).encode("utf-8")
        except UnicodeEncodeError:
            pass
        else:
            raise TestFailed("chr(%d).encode('utf-8') should raise "
                             "UnicodeEncodeError" % i)

    for i in range(0xD800, 0xE000):
        try:
            s = chr(i).encode("utf-8", "add_one_codepoint")
        except UnicodeEncodeError:
            raise TestFailed("chr(%d).encode('utf-8', 'add_one_codepoint') "
                             "shouldn't raise UnicodeEncodeError" % i)
        else:
            if s != b'a':
                raise TestFailed("chr(%d).encode('utf-8', 'add_one_codepoint') "
                                 "should return b'a
