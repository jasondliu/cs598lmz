import codecs
# Test codecs.register_error

def handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test', handler)

def test(encoding):
    print '-'*20, encoding, '-'*20
    try:
        u = unicode('abc\x80def', encoding, 'test')
    except UnicodeError, detail:
        print 'ERROR:', detail
    else:
        print 'u =', u.encode(encoding)

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test(encoding)

# Test codecs.lookup_error

def handler(exception):
    return (u'\ufffd', exception.end)

def test(encoding):
    print '-'*20, encoding, '-'*20
    try:
        u = unicode('abc\x80def', encoding, 'test')
    except UnicodeError, detail:
        print 'ERROR:', detail
    else:
        print 'u =', u.
