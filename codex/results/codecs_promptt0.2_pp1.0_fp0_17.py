import codecs
# Test codecs.register_error

# This test is for the case where the error handler is a function
# that takes a UnicodeDecodeError as its argument.

def handler(e):
    return (u'\ufffd', e.end)

codecs.register_error('test.unicode_decode_error', handler)

def test(encoding):
    try:
        u'abc\xff'.decode(encoding)
    except UnicodeDecodeError, e:
        print e.__class__.__name__, e
        print 'start:', e.start
        print 'end:', e.end
        print 'object:', repr(e.object)
        print 'reason:', e.reason
        print 'encoding:', e.encoding
        print 'end:', e.end
        print 'object:', repr(e.object)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print encoding
    test(encoding)
    print '-'*20
