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
    # test for http://bugs.python.org/issue11395
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for error_handler in ('strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            try:
                codecs.decode(b'\xff', encoding, error_handler)
            except UnicodeDecodeError as e:
                assert e.start == 0
                assert e.end == 1
                assert e.reason == 'invalid continuation byte'
                assert e.object == b'\xff'
                assert e.encoding == encoding
            else:
                assert error_handler in ('replace', 'ignore')

if __name__ == "__main__":
    test_main()
