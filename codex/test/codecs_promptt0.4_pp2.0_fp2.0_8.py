import codecs
# Test codecs.register_error
def test_register_error():
    def handler(exc):
        if isinstance(exc, UnicodeEncodeError):
            return (u'', exc.end)
        elif isinstance(exc, UnicodeDecodeError):
            return (u'', exc.end)
        else:
            raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error('test.ignore', handler)
    assert codecs.lookup_error('test.ignore') is handler
    #
    assert codecs.strict_errors == 'strict'
    codecs.strict_errors = 'test.ignore'
    assert codecs.strict_errors == 'test.ignore'
    codecs.strict_errors = 'strict'
    #
    assert codecs.ignore_errors == 'ignore'
    codecs.ignore_errors = 'test.ignore'
    assert codecs.ignore_errors == 'test.ignore'
    codecs.ignore_errors = 'ignore'
    #
    assert codecs.replace_errors == 'replace'

