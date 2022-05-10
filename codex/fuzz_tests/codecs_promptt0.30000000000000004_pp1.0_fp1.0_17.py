import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print '-'*30
    print 'Encoding', encoding
    print '-'*30
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.lookup')
        print repr(s)
    except UnicodeError, detail:
        print 'ERROR:', detail

for encoding in ['iso8859-1', 'iso8859-2', 'iso8859-3', 'iso8859-4',
                 'iso8859-5', 'iso8859-6', 'iso8859-7', 'iso8859-8',
                 'iso8859-9', 'iso8859-10', 'iso8859-11', 'iso8859-13',
                 'iso8859-14', 'iso88
