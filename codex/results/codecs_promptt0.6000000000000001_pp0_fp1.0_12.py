import codecs
# Test codecs.register_error()

import codecs

def test_errors(name):
    print 'Testing error handler', name, '...'
    print 'Testing unicode(string, encoding) with', name, '...'
    u = unicode('\x99', 'latin1', name)
    print 'Testing unicode.encode() with', name, '...'
    s = u.encode('utf-16', name)
    print 'Testing unicode.encode() with', name, '...'
    s = u.encode('utf-16', name)
    print 'Testing string.decode() with', name, '...'
    u = '\xff\xfe\x99\x00'.decode('utf-16', name)

codecs.register_error('test-error-handler', test_errors)

print 'Testing unicode(string, encoding) with test-error-handler ...'
u = unicode('\x99', 'latin1', 'test-error-handler')
print 'Testing unicode.encode() with test-error-handler ...'

