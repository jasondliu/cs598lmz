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
    # test UnicodeEncodeError
    for encoding in ('ascii', 'utf-8', 'utf-16', 'utf-32'):
        for code in [0xffff, 0x10000, 0x10ffff]:
            try:
                unichr(code).encode(encoding)
            except UnicodeEncodeError as exc:
                if encoding == 'ascii':
                    assert exc.end == exc.start + 1
                    assert exc.object[exc.start] == unichr(code)
                elif encoding == 'utf-8':
                    assert exc.end == exc.start + 3
                    assert exc.object[exc.start:exc.end] == unichr(code).encode('utf-8')
                elif encoding == 'utf-16':
                    assert exc.end == exc.start + 1
                    assert exc.object[exc.start:exc.end] == unichr(code).encode('utf-16')
                else:
                    assert exc.end == exc.start + 1
                    assert exc.object[
