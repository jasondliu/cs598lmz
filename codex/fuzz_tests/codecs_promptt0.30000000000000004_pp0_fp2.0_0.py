import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print '-'*20, encoding, '-'*20
    try:
        u'\u3042'.encode(encoding)
    except UnicodeEncodeError, e:
        print 'ERROR:', e
        print 'BACKTRACE:'
        traceback.print_exc()
    print '-'*50

test('ascii')
test('test.lookup')
