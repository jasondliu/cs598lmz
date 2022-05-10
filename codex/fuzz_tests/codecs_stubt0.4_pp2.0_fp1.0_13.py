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
    # UTF-8
    for encoding in ('utf-8', 'utf_8', 'UTF-8', 'UTF_8'):
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            for b in (b'abc', b'\xc2\x80', b'\xe0\xa0\x80', b'\xf0\x90\x80\x80', b'\xf8\x88\x80\x80\x80', b'\xfc\x84\x80\x80\x80\x80'):
                try:
                    u = b.decode(encoding, errors)
                except UnicodeDecodeError as exc:
                    if errors == 'strict':
                        pass
                    elif errors == 'replace':
                        assert u'\ufffd' in u
                    elif errors == 'ignore':
                        assert len(u) == 0
                    elif errors == 'add_one_
