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
    # test surrogatepass
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'surrogatepass'):
            for data in (b'\xed\xa0\x80', b'\xed\xa0\x80\xed\xb0\x80'):
                try:
                    data.decode(encoding, errors)
                except UnicodeDecodeError:
                    pass
                else:
                    raise AssertionError("surrogatepass should fail")

    # test backslashreplace
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'backslashreplace'):
            for data in (b'\xed\xa0\x80', b'\xed\xa0\x80\xed\xb0\x80'):
                try:
                    data.decode(encoding, errors)
                except UnicodeDecodeError:
                    pass
                else:
                    raise
