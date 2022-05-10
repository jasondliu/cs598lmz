import codecs
# Test codecs.register_error()

def test_register_error():
    # UnicodeEncodeError
    def raise_exc(exc):
        raise exc

    def replace_exc(exc):
        if not isinstance(exc, UnicodeEncodeError):
            raise TypeError("don't know how to handle %r" % exc)
        return (u'', exc.end)

    def ignore_exc(exc):
        if not isinstance(exc, UnicodeEncodeError):
            raise TypeError("don't know how to handle %r" % exc)
        return (u'', exc.end)

    def xmlcharrefreplace_exc(exc):
        if not isinstance(exc, UnicodeEncodeError):
            raise TypeError("don't know how to handle %r" % exc)
        return (u'', exc.end)

    def backslashreplace_exc(exc):
        if not isinstance(exc, UnicodeEncodeError):
            raise TypeError("don't know how to handle %r" % exc)
        return (u'', exc.end)

    # UnicodeDecodeError
