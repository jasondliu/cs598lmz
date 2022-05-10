import codecs
# Test codecs.register_error

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        return ("?", exc.end)
    elif isinstance(exc, UnicodeEncodeError):
        return ("?", exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def strict_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        raise exc
    elif isinstance(exc, UnicodeEncodeError):
        raise exc
    else:
        raise TypeError("don't know how to handle %r" % exc)


def test_decode(encoding):
    # Test decoding
    codecs.register_error("test.replace", replace_error)
    codecs.register_error("test.strict", strict_error)
    for errors in ["strict", "replace", "ignore", "test.strict", "test.replace"]:
        if errors == "strict":
            # "strict" is a builtin error handler
            continue
