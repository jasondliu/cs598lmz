import codecs
# Test codecs.register_error

import codecs

def raise_exc(exc):
    raise exc

def test(encoding):
    print '-'*50
    print 'Encoding:', encoding
    print '-'*50
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        print 'UCS2 string:', repr(u)
        print 'UTF8    :', repr(u.encode('utf-8'))
        print 'UCS2    :', repr(u.encode('unicode-internal'))
        print 'default :', repr(u.encode())
        print
        print 'Registering error handler'
        codecs.register_error('test', raise_exc)
        print 'Encoding with errors=test'
        print 'UTF8    :', repr(u.encode('utf-8', 'test'))
        print 'UCS2    :', repr(u.encode('unicode-internal', 'test'))
        print 'default :', repr(u.encode('test
