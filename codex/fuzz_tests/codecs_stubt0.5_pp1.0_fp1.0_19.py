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

def check_exception(encoding, text, errors, handler=None):
    # Check that the specified error handler is called when decoding
    # the specified text with the specified error handling.
    # If handler is None, check that the default handler is called.
    # Returns the number of times the handler was called.
    #
    # The handler is called with an exception instance as argument.
    # If the handler returns a tuple, the first element is inserted
    # into the decoded text, and the second is used as the new
    # position in the input buffer.
    #
    # For example, the following handler is called twice when
    # decoding '\x80\x80' with the "replace" error handler:
    #
    # def handler(exc):
    #     print("called")
    #     return ("?", exc.start)
    #
    # For example, the following handler is called once when
    # decoding '\x80\x80' with the "ignore" error handler:
    #
    # def handler(exc):
    #     print("called")
    #
