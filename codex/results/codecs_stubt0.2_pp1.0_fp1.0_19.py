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
    # test codecs.register_error()
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            try:
                codecs.decode(b'\xff', encoding, errors)
            except UnicodeDecodeError as exc:
                if errors == 'strict':
                    raise
                elif errors == 'replace':
                    assert exc.object == b'\xff'
                    assert exc.start == 0
                    assert exc.end == 1
                    assert exc.reason == 'illegal multibyte sequence'
                elif errors == 'ignore':
                    assert exc.object == b'\xff'
                    assert exc.start == 0
                    assert exc.end == 1
                    assert exc.reason == 'illegal multibyte sequence'
                elif errors == 'add_one_codepoint':
                    assert exc.object == b'\xff
