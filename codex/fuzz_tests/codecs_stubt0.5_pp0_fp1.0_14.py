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
    # UnicodeDecodeError
    for encoding in ['latin-1', 'utf-16', 'utf-32']:
        for strict in [True, False]:
            for reason in ['illegal', 'undefined', 'surrogatepass']:
                try:
                    codecs.decode(b'\x80', encoding, reason)
                except UnicodeDecodeError as exc:
                    if reason == 'illegal':
                        if strict:
                            assert exc.object == b'\x80'
                            assert exc.start == 0
                            assert exc.end == 1
                        else:
                            assert exc.object == b'\x80'
                            assert exc.start == 0
                            assert exc.end == 1
                    else:
                        assert exc.object == b'\x80'
                        assert exc.start == 0
                        assert exc.end == 1
                else:
                    assert False, 'expected UnicodeDecodeError'

                try:
                    codecs.decode(b'\x80', encoding, reason, 'add_one_cod
