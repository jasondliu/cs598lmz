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

utf8_decoder = codecs.getincrementaldecoder("utf-8")()
utf8_decoder.set_error_handler(add_one_codepoint)
utf8_encoder = codecs.getincrementalencoder("utf-8")()
utf8_encoder.set_error_handler(add_utf16_bytes)

utf16_decoder = codecs.getincrementaldecoder("utf-16")()
utf16_decoder.set_error_handler(add_utf8_bytes)
utf16_encoder = codecs.getincrementalencoder("utf-16")()
utf16_encoder.set_error_handler(add_one_codepoint)

utf32_decoder = codecs.getincrementaldecoder("utf-32")()
utf32_decoder.set_error_handler(add_utf8_bytes)
utf32_encoder = codecs.getincrementalencoder("utf-32")()
utf32_encoder.set_error_handler(add_one_codepoint)
