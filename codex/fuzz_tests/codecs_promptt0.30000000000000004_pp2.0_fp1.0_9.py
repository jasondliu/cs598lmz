import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print '-'*20, encoding, '-'*20
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.lookup')
        print repr(s)
    except UnicodeError, detail:
        print 'UnicodeError:', detail

for encoding in ['iso8859-1', 'iso8859-2', 'iso8859-15', 'koi8-r', 'ascii',
                 'utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'utf-32',
                 'utf-32-le', 'utf-32-be', 'unicode-internal']:
    test(encoding)

# Test codecs.register_error() with a function

def handler(
