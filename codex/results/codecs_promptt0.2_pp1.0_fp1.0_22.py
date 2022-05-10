import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', my_error_handler)

# Test the registered error handler

print 'TEST 1'
for encoding in ('test.myerror', 'test.myerror', 'test.myerror'):
    print 'ENCODING:', encoding
    print '  u"\u3042".encode(%s)' % encoding
    print '  ', repr(u"\u3042".encode(encoding))
    print '  u"\u3042\u3044".encode(%s)' % encoding
    print '  ', repr(u"\u3042\u3044".encode(encoding))
    print '  u"\u3042\u3044\u3046".encode(%s)' % encoding
    print '  ', repr(u"\u3042\u3044\u3046".encode(
