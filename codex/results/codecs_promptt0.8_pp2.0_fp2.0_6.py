import codecs
# Test codecs.register_error()
def repr_exception(exc):
    if isinstance(exc, UnicodeDecodeError):
        return 'UnicodeDecodeError: %s' % \
                 evilunicode.decode(exc.object[exc.start:exc.end],
                                    exc.encoding, 'replace')
    elif isinstance(exc, UnicodeEncodeError):
        return 'UnicodeEncodeError: %r' % \
                 evilunicode.encode(exc.object[exc.start:exc.end],
                                    exc.encoding, 'replace')
    return repr(exc)

def search_function(exc):
    # For testing purposes, decode all errors as X, and encode all
    # non-ASCII characters as \uXXXX. We don't need to worry about
    # UnicodeEncodeErrors since 1.4, because the encoder will
    # automatically call the registered error handler for encode()
    # operations.
    if isinstance(exc, UnicodeDecodeError):
        # Note: the failure case here is UnicodeEncodeError, which
        # will be caught
