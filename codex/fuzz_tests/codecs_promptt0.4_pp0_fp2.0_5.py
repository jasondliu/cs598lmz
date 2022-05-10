import codecs
# Test codecs.register_error()
def test_register_error():
    def handler(exc):
        if isinstance(exc, UnicodeDecodeError):
            x, y = exc.object[exc.start:exc.end], exc.reason
            print 'UnicodeDecodeError:', x, y
            return (u'', exc.end)
        raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error('test.ignore', handler)
    codecs.register_error('test.replace', handler)
    codecs.register_error('test.xmlcharrefreplace', handler)
    codecs.register_error('test.backslashreplace', handler)
    codecs.register_error('test.namereplace', handler)
    codecs.register_error('test.strict', handler)
    codecs.register_error('test.ignore', None)
    codecs.register_error('test.replace', None)
    codecs.register_error('test.xmlcharrefreplace', None)
    codecs.register_error('test.backslashreplace
