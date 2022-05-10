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

def test_general_unicode_decode_error(test_support):
    # test general UnicodeError handling for codecs.decode()
    for name in ('ascii', 'latin-1', 'utf-8'):
        # test UnicodeDecodeError
        for (input, start, end) in (
            ("abc\xe4\xe4", 3, 4), # incomplete multibyte character
            ("abc\xe4\xe4\xff", 3, 6), # incomplete with trailing byte
            ("abc\xe4\xe4\xff", 3, 5), # incomplete with trailing byte
            ("abc\xe4\xe4\xff", 3, 4), # incomplete with trailing byte
            ):
            exc = None
            try:
                codecs.decode(input, name)
            except UnicodeDecodeError, exc:
                pass
            if not exc:
                test_support.TestError(
                    "codecs.decode() didn't raise UnicodeDecodeError "
                    "for input=%r, error handler=None" % (input,))
           
