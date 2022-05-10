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

# UTF-16 encoder (BE)
def encode_utf16be(input, errors='strict'):
    return codecs.utf_16_encode(input, errors, True)

# UTF-16 decoder (BE)
def decode_utf16be(input, errors='strict'):
    return codecs.utf_16_decode(input, errors, True)

# UTF-16-LE encoder/decoder
codecs.register(lambda name: codecs.lookup('utf-16')
                if name == 'cp65001' else None)

# UTF-32 encoder (BE)
def encode_utf32be(input, errors='strict'):
    return codecs.utf_32_encode(input, errors, True)

# UTF-32 decoder (BE)
def decode_utf32be(input, errors='strict'):
    return codecs.utf_32_decode(input, errors, True)

# UTF-32-LE encoder/decoder
codecs.register(lambda name: codecs
