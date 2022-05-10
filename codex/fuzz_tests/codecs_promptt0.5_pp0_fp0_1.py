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
    except Exception, err:
        print "Unexpected exception", err

def check_decode(input, errors):
    try:
        input.decode("ascii", errors)
    except UnicodeDecodeError:
        pass
    except Exception, err:
        print "Unexpected exception", err

# Register the error handler under a name
codecs.
