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

def test_decode_error(decode_func, *args, **kwargs):
    try:
        decode_func(*args, **kwargs)
    except UnicodeDecodeError as e:
        return e
    else:
        raise AssertionError("UnicodeDecodeError not raised")

def test_encode_error(encode_func, *args, **kwargs):
    try:
        encode_func(*args, **kwargs)
    except UnicodeEncodeError as e:
        return e
    else:
        raise AssertionError("UnicodeEncodeError not raised")

def test_decode_error_add_one_codepoint(decode_func, *args, **kwargs):
    try:
        decode_func(*args, **kwargs)
    except UnicodeDecodeError as e:
        return e
    else:
        raise AssertionError("UnicodeDecodeError not raised")

def test_encode_error_add_one_codepoint(encode_func, *args, **kw
