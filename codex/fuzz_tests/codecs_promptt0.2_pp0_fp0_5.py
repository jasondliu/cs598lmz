import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print '-'*20, encoding
    try:
        u'\u3042'.encode(encoding, 'test.lookup')
    except UnicodeEncodeError, detail:
        print detail

test('ascii')
test('iso-8859-1')
test('iso-8859-15')
test('utf-8')
test('utf-16')
test('utf-16-le')
test('utf-16-be')
test('utf-32')
test('utf-32-le')
test('utf-32-be')
test('unicode-internal')
test('raw-unicode-escape')
test('unicode-escape')
test('unicode-escape')
test('string-escape')
test('latin-1')
test('iso-8859-1')
test('cp037')
test('cp424')
test('cp437')
