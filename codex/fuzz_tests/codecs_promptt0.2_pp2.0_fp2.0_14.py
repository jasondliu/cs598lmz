import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

def test(encoding):
    print '-'*20, encoding, '-'*20
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.ignore')
        print repr(s), repr(u.encode(encoding))
    except LookupError, v:
        print 'ERROR:', v

for encoding in ['iso8859-1', 'iso8859-2', 'iso8859-3', 'iso8859-4',
                 'iso8859-5', 'iso8859-6', 'iso8859-7', 'iso8859-8',
                 'iso8859-9', 'iso8859-10', 'iso8859-11', 'iso8859-13',
                 'iso8859-14', 'iso8859-15', 'iso8859-16
