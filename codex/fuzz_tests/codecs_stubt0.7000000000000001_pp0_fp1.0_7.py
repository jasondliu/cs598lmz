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

def encode_utf8(text):
    return text.encode('utf-8', 'add_one_codepoint')

def decode_utf8(text):
    return text.decode('utf-8', 'add_one_codepoint')

def encode_utf16(text):
    return text.encode('utf-16', 'add_utf16_bytes')

def decode_utf16(text):
    return text.decode('utf-16', 'add_utf16_bytes')

def encode_utf32(text):
    return text.encode('utf-32', 'add_utf32_bytes')

def decode_utf32(text):
    return text.decode('utf-32', 'add_utf32_bytes')

def encode_utf32_be(text):
    return text.encode('utf-32-be', 'add_utf32_bytes')

def decode_utf32_be(text):
    return text.decode('utf-32-be', 'add_utf32_bytes')

def encode_
