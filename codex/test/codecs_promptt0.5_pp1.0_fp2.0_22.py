import codecs
# Test codecs.register_error
import codecs

def unicode_error_handler(exception):
    return (u'', exception.end)

def test_register_error():
    codecs.register_error('test.unicode', unicode_error_handler)
    s = u'abc\uDC80def'
    assert codecs.decode(s.encode('ascii', 'test.unicode'), 'ascii') == u'abcdef'

def test_register_error_twice():
    codecs.register_error('test.unicode', unicode_error_handler)
    codecs.register_error('test.unicode', unicode_error_handler)
    s = u'abc\uDC80def'
    assert codecs.decode(s.encode('ascii', 'test.unicode'), 'ascii') == u'abcdef'

def test_lookup_error():
    codecs.register_error('test.unicode', unicode_error_handler)
    s = u'abc\uDC80def'
