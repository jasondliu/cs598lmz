import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

def test(encoding):
    print '-'*20, encoding, '-'*20
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        print 'UCS2:', repr(u)
        s = u.encode(encoding, 'test.ignore')
        print 'ENCODED:', repr(s)
        u2 = s.decode(encoding, 'test.ignore')
        print 'DECODED:', repr(u2)
    except UnicodeError, detail:
        print 'ERROR:', detail

for encoding in ['iso8859-1', 'iso8859-15', 'ascii', 'latin-1']:
    test(encoding)

print '-'*20, 'UTF-7', '-'*20
try:
    u = u'\u3042\u3044\u30
