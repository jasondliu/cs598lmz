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
#   Testing UTF-8
#

encoding = "utf-8"
test_support.verbose = 1

def decode_errorhandler_test(input, errors):
    # If a UnicodeDecodeError is to be raised, the faulty character
    # is in the second byte of the input string.
    assert input[1] == '\xf4'
    decoder = codecs.getincrementaldecoder(encoding)(errors)
    decoder.decode(input[:1]), decoder.decode(input[1:], True)

def encode_errorhandler_test(errors):
    # If an UnicodeEncodeError is to be raised, errors must be
    # "strict", and the faulty character is always \udc80.
    assert errors == "strict"
    return ("abc", 1+0xd800)

def encode_errorhandler_xmlcharrefreplace_test(errors):
    # Check for xmlcharrefreplace error handler and broad
    # spectrum of characters.
    assert errors == "xmlcharrefreplace"
    return tuple(
