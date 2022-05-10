import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

def test(encoding):
    print '-'*30
    print 'Encoding:', encoding
    print 'encode:', repr(u'\u3042\u3044\u3046\u3048\u304a')
    print 'decode:', repr('\xa4\xa2\xa4\xa4\xa4\xa6\xa4\xa8\xa4\xaa')
    print '-'*30
    print 'Without error handler'
    try:
        print 'encode:', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding))
    except UnicodeEncodeError, err:
        print 'ERROR:', err
    try:
        print 'decode:', repr('\xa4\xa2\xa4\xa4\xa4\xa6\xa4\xa8\xa4\xaa'.
