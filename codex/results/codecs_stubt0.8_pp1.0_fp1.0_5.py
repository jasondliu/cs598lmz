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

# not needed anymore since bytes path has been fixed in 2.7.12
# ##############################################################################
# # Test for bug #1001456:  UTF-16/UTF-32 decoder does not detect errors when
# # reading only part of the byte sequence
#
# def test_bug1001456_utf16(dec):
#     proper_bytes, not_enough_bytes, too_many_bytes = \
#                     codecs.getincrementaldecoder(dec)().iterencode(b"abc")
#     for errorhandler in ["strict", "ignore", "replace", "add_one_codepoint"]:
#         for bytes in (not_enough_bytes, too_many_bytes):
#             msg = ("b'%s' failed with error handler '%s'" %
#                 (codecs.escape_encode(bytes)[0], errorhandler))
#             assert (codecs.decode(bytes, dec, errorhandler)
#                         == codecs.decode(proper_bytes, dec, errorhandler)), msg
#             if errorhandler
