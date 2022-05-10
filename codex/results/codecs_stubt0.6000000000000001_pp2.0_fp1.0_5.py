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

def py_decode(data, encoding, errors):
    return codecs.decode(data, encoding, errors)

def py_encode(data, encoding, errors):
    return codecs.encode(data, encoding, errors)

def test_decode(encoding):
    encoding = encoding.lower()
    if encoding.startswith("utf-16"):
        s = b'\xff\xfe'
    elif encoding.startswith("utf-32"):
        s = b'\xff\xfe\x00\x00'
    else:
        s = b''
    s += b'\x00\x01\x7f\x80\xff\x00\xff\x01\x7f\x80\x80\xff'
    s += b'\x00\x00\x01\x7f\x00\xff\x01\x7f\x80\x00\xff\x01\x7f\x80\x80\x00\xff'
    s += b'\x00
