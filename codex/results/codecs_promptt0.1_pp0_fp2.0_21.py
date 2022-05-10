import codecs
# Test codecs.register_error

import codecs

def test_register_error():
    def my_error_handler(exception):
        return (u'', exception.end)

    codecs.register_error('test.myerrorhandler', my_error_handler)
    s = '\x80abc'
    u = s.decode('ascii', 'test.myerrorhandler')
    assert u == u'abc'
    assert type(u) is unicode

def test_register_error_with_name():
    def my_error_handler(exception):
        return (u'', exception.end)

    codecs.register_error('test.myerrorhandler', my_error_handler, 'myerrorhandler')
    s = '\x80abc'
    u = s.decode('ascii', 'myerrorhandler')
    assert u == u'abc'
    assert type(u) is unicode

def test_register_error_with_unicode():
    def my_error_handler(exception):
        return (u'', exception.end)

   
