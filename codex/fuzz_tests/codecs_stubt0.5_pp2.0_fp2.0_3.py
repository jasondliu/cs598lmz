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

# The codecs module also has a register_error() function which can be used to
# register error handling functions.
#
# A codec error handling function must take two arguments, an exception
# instance and a position in the input string where the error occurred. It
# must either raise a UnicodeDecodeError or UnicodeEncodeError exception, or
# return a tuple (replacement, new position) where replacement is either a
# Unicode string or a character code, and new position is an integer.
#
# The following example shows how to register a function to handle
# UnicodeDecodeError exceptions by replacing them with the Unicode character
# U+FFFD, the Unicode replacement character.

def replace_with_fffd(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.start)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("replace_with_fffd", replace_with_fffd)

# The following example shows how to register a function to handle
# UnicodeEncode
