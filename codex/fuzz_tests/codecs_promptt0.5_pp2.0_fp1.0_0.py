import codecs
# Test codecs.register_error
def raise_exc(exc):
    raise exc

codecs.register_error("test.raise_exc", raise_exc)

def test_codecs_register_error(encoding):
    # Encoding that raise UnicodeEncodeError
    try:
        u"\u3042".encode(encoding, "test.raise_exc")
    except UnicodeEncodeError:
        pass
    else:
        print("Didn't raise UnicodeEncodeError for", encoding)

    # Encoding that raise UnicodeDecodeError
    try:
        b"\x80".decode(encoding, "test.raise_exc")
    except UnicodeDecodeError:
        pass
    else:
        print("Didn't raise UnicodeDecodeError for", encoding)


def test_codecs_register_error_surrogateescape(encoding):
    # Encoding that raise UnicodeEncodeError
    try:
        u"\u3042".encode(encoding, "surrogateescape")
    except UnicodeEncodeError:
        pass
    else:
