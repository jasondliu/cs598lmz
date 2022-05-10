import codecs
# Test codecs.register_error()

def handler(exception):
    print 'handler:', exception
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def search_function(encoding):
    print 'search_function:', encoding
    if encoding == 'test.lookup':
        return codecs.lookup_error('test.lookup')
    return None

codecs.register(search_function)

s = 'abc\x80\x80\xc0'
for encoding in ['ascii', 'test.lookup']:
    print 'ENCODING:', encoding
    try:
        u = s.decode(encoding)
    except UnicodeDecodeError, e:
        print 'ERROR:', e
    else:
        print 'OK:', repr(u)
