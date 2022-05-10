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

encoding = 'utf-8'
correct_unicode = '%s₀%s' % (encoding, encoding)

def raise_error(encoding, hint, correct_unicode):
       try:
               correct_unicode.encode(encoding, hint)
       except codecs.UnicodeEncodeError as exc:
               if hint == "ignore":
                       # Cause the error again to trigger the caller's except clause
                       raise ValueError('Failed to encode unicode as %s!' % encoding)
               print('Hello from codec exception handler!')
               return exc
       else:
               # Shouldn't get here
               raise ValueError('No exception raised!')

def test_util_codecs(encoding):
    encoding = 'utf-8'
    correct_unicode = '%s₀%s' % (encoding, encoding)

    # Check that 'raise' is the default
    exc = raise_error(encoding, "", correct_unicode)
    assert str(exc) == 'Can\'t encode character "₀
