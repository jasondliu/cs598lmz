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

# This tests that a UnicodeEncodeError is raised by the UTF-7 encoder.
# During the encoding of character '\u2028', the error handler "replace" is
# called and replaces the character by '?' characters, raising an
# UnicodeEncodeError (to mimic a wrong error handler behaviour).
try:
    bytes("?\u2028", "utf-7")
except UnicodeEncodeError as err:
    if (err.object != "?\u2028" or err.encoding != "utf-7" or
        err.start != 0 or err.end != 2 or err.reason != "surrogates not allowed"):
            raise AssertionError("wrong UnicodeEncodeError raised")
    # This has to check the error object of the UnicodeEncodeError.
    # The exception should have an error attribute that is a tuple of
    # (encoding, code, startpos, endpos). It returns a 3-tuple.
    # The ending position should be 2 (the index of the second characters in
    # the string).
    errobj = err.object
    assert(
