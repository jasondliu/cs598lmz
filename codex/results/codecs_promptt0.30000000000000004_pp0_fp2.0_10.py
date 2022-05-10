import codecs
# Test codecs.register_error()

def handler(exception):
    print '***', exception
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

def test(encoding):
    print encoding, ':',
    try:
        unicode(b'\x80', encoding, 'test.ignore')
    except UnicodeDecodeError as e:
        print 'ERROR:', e
    else:
        print 'OK'

test('ascii')
test('latin-1')
test('iso8859-1')
test('iso8859-15')
test('cp1252')
test('utf-8')
test('utf-16')
test('utf-16-le')
test('utf-16-be')
test('utf-32')
test('utf-32-le')
test('utf-32-be')
test('unicode-escape')
test('raw-unicode-escape')
test('unicode-internal')

# Test codecs.register_error()

def handler(exception):
    print
