import codecs
# Test codecs.register_error

import codecs

def my_error(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error)

def test(encoding):
    print '-'*20, encoding
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'my_error')
        print 'encode:', s, repr(s)
        print 'decode:', s.decode(encoding, 'my_error')
    except UnicodeError, e:
        print 'ERROR:', e

for encoding in ['iso8859-1', 'iso8859-2', 'iso8859-3', 'iso8859-4',
                 'iso8859-5', 'iso8859-6', 'iso8859-7', 'iso8859-8',
                 'iso8859-9', 'iso8859-10', 'iso8859-11', 'iso8859-13',
                
