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

