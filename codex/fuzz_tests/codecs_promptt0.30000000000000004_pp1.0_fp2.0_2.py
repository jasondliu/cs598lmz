import codecs
# Test codecs.register_error()

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

def test(name):
    print '%s:' % name
    for input in ['abc', '\x80', '\x80\x80', '\x80\x80\x80', '\x80\x80\x80\x80']:
        print ' ', input, '->',
        try:
            print input.decode(name, 'test.lookup'),
        except UnicodeError, e:
            print 'UnicodeError:', e,
        print

test('utf-8')
test('utf-16')
test('utf-16-le')
test('utf-16-be')
test('utf-32')
test('utf-32-le')
test('utf-32-be')
test('iso-8859-1')
test('ascii')
test('latin-1')

print 'Done'
