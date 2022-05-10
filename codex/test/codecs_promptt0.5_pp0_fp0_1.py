import codecs
# Test codecs.register_error

# Encoding error handler that raises UnicodeEncodeError
def raise_encode_exception(exc):
    if isinstance(exc, UnicodeEncodeError):
        raise exc
    else:
        raise TypeError("don't know how to handle %r" % exc)

# Decoding error handler that raises UnicodeDecodeError
def raise_decode_exception(exc):
    if isinstance(exc, UnicodeDecodeError):
        raise exc
    else:
        raise TypeError("don't know how to handle %r" % exc)

def check_encode(input, errors):
    try:
        input.encode("ascii", errors)
    except UnicodeEncodeError:
        pass
