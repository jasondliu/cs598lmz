import codecs
# Test codecs.register_error()

# Encoded unicode string
t = b'\xc3\xa9rreur'

def xtest_register_error():
    # Register an error handler that works on char and treats each
    # byte as a character
    def charerror(exc):
        if not isinstance(exc, UnicodeDecodeError):
            raise TypeError("don't know how to handle %r" % exc)
        return (unicode(chr(exc.object[exc.start]), 'latin-1'), exc.start+1)
    codecs.register_error('CHARSIGNORE', charerror)

    # Test that the error handler is called
    u = unicode(t, 'ascii', 'CHARSIGNORE')
    assert u == u'\xe9rreur'

    # Try encoding back from unicode and test that the error handler is
    # called and that the result is the same as for decoding with
    # 'replace'
    v = u.encode('ascii', 'backslashreplace')
