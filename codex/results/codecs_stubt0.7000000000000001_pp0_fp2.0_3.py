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


def utf8_decode(input, errors='strict'):
    return (input.replace(b'\x80', b'a'), len(input))

def utf8_encode(input, errors='strict'):
    return (input.replace('\x80', 'a').encode('utf-8'), len(input))

def utf16_le_decode(input, errors='strict'):
    return (input.decode('utf-16-le', errors), len(input))

def utf16_be_decode(input, errors='strict'):
    return (input.decode('utf-16-be', errors), len(input))

def utf16_encode(input, errors='strict'):
    return (input.encode('utf-16', errors), len(input))

def utf32_le_decode(input, errors='strict'):
    return (input.decode('utf-32-le', errors), len(input))

def utf32_be_decode
