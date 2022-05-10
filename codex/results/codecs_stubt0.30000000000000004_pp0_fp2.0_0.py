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
    # Test that the codecs module can be used to add a character to a
    # UnicodeDecodeError object.
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        try:
            codecs.decode(b'\xff', encoding)
        except UnicodeDecodeError as exc:
            if encoding == 'utf-8':
                new_exc = codecs.lookup_error("add_one_codepoint")(exc)
            elif encoding == 'utf-16':
                new_exc = codecs.lookup_error("add_utf16_bytes")(exc)
            elif encoding == 'utf-32':
                new_exc = codecs.lookup_error("add_utf32_bytes")(exc)
            assert new_exc.object == b'\xff'
            assert new_exc.start == 0
            assert new_exc.end == 1
            assert new_exc.reason == 'invalid start byte'
            assert new_exc.encoding == encoding
            assert new_exc
