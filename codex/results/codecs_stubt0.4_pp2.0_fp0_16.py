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
    for encoding in ('utf-32', 'utf-32-le', 'utf-32-be'):
        # test decode
        for errorhandler in ('strict', 'ignore', 'replace', 'add_one_codepoint', 'add_utf32_bytes'):
            try:
                codecs.decode(b'\xff', encoding, errorhandler)
            except UnicodeDecodeError as e:
                if errorhandler == 'strict':
                    pass
                elif errorhandler == 'ignore':
                    assert e.object == b'\xff'
                    assert e.start == 0
                    assert e.end == 1
                    assert e.reason == 'invalid continuation byte'
                elif errorhandler == 'replace':
                    assert e.object == b'\xff'
                    assert e.start == 0
                    assert e.end == 1
                    assert e.reason == 'invalid continuation byte'
                elif errorhandler == 'add_one_codepoint':
                    assert e.object == b'\xff'
                    assert e.start == 0

