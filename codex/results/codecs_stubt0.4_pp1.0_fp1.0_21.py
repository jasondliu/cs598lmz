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
    for encoding in ['utf-8', 'utf-16', 'utf-32']:
        for errors in ['strict', 'replace', 'ignore', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes']:
            print(encoding, errors)
            try:
                codecs.decode('\xff', encoding, errors)
            except UnicodeDecodeError as exc:
                if errors == 'strict':
                    pass
                elif errors == 'replace':
                    assert exc.object == b'\xff'
                    assert exc.start == 0
                    assert exc.end == 1
                    assert exc.reason == 'invalid continuation byte'
                    assert exc.encoding == encoding
                    assert exc.args[0] == 'invalid continuation byte'
                    assert exc.args[1] == b'\xff'
                    assert exc.args[2] == 0
                    assert exc.args[3] == 1
                    assert exc.args[4] == encoding
                elif errors == 'ignore':
                   
