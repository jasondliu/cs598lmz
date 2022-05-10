import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test', handler)

def test_register_error():
    assert codecs.lookup_error('test') is handler
    assert codecs.lookup_error('test')(Exception()) == (u'\ufffd', None)
    raises(TypeError, codecs.lookup_error, 'test', 'test')

def test_register_error_overwrite():
    def handler(exception):
        return (u'\ufffd', exception.end)
    codecs.register_error('test', handler)
    assert codecs.lookup_error('test') is handler
    assert codecs.lookup_error('test')(Exception()) == (u'\ufffd', None)

def test_register_error_unicode():
    def handler(exception):
        return (u'\ufffd', exception.end)
    codecs.register_error(u'test', handler)
    assert codecs
