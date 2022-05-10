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
    # Test surrogatepass error handler
    for enc in ('utf-8', 'utf-16', 'utf-32'):
        for i in range(0xd800, 0xdc00):
            with support.check_warnings(('', DeprecationWarning)):
                s = chr(i).encode(enc, 'surrogatepass')
            assert s == bytes(enc, 'surrogatepass')[i:i+1]
        for i in range(0xdc00, 0xe000):
            with support.check_warnings(('', DeprecationWarning)):
                s = chr(i).encode(enc, 'surrogatepass')
            assert s == bytes(enc, 'surrogatepass')[i:i+1]

    # Test backslashreplace error handler
    for enc in ('utf-8', 'utf-16', 'utf-32'):
        for i in range(0xd800, 0xdc00):
            with support.check_warnings(('', DeprecationWarning)):
               
