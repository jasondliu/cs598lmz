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

#
# UnicodeDecodeError and UnicodeEncodeError are expected to cause
# an exception and are therefore not tested for.
#
# ATTENTION!
#
# Do NOT add new tests that specify unicode character strings as
# arguments to error handlers!!!  That will break on narrow unicode
# builds because the UnicodeDecodeError and UnicodeEncodeError
# attributes are of type 'str' there, and the type 'str' in narrow
# unicode builds is "ucs2", not "utf8" or "utf16".  A false match
# would occur.
#
# The error handlers can be tested with bytes/bytearray/memoryview as
# arguments however, like this:
#
#    b'\r\n'.decode('ascii', errors='backslashreplace')
#
enctests = [

    # single-character string
    (u'\ud320'.encode('utf7', 'add_one_codepoint'), '+AFwA-'),
    (BufferedIncrementalEncoder('utf7',
                                errors='add_one_codep
