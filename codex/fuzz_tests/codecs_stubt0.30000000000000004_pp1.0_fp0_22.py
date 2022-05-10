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

# This is a list of all the codecs that are known to have a
# UnicodeDecodeError handler.  The UnicodeDecodeError handler is
# responsible for inserting the replacement character.  If it doesn't
# do that, then the error handler will be called, and the error handler
# will insert the replacement character.
#
# The codecs that are known to have a UnicodeDecodeError handler are:
#
#   ascii
#   latin-1
#   utf-8
#   utf-16
#   utf-16-le
#   utf-16-be
#   utf-32
#   utf-32-le
#   utf-32-be
#
# The codecs that are known to not have a UnicodeDecodeError handler
# are:
#
#   big5
#   big5hkscs
#   cp037
#   cp424
#   cp437
#   cp500
#   cp720
#   cp737
#   cp775
#   cp850
#   cp852
#   cp
