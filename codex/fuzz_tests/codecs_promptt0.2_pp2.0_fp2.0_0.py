import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

u = u'\u3042\u3044\u3046\u3048\u304a'

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32']:
    print 'Trying', encoding
    try:
        s = u.encode(encoding, 'test.lookup')
    except UnicodeEncodeError, detail:
        print 'UnicodeEncodeError:', detail
    else:
        print 'No exception, s =', s

# Test codecs.register_error with a function

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

u = u'\u3042\u3044\u3046\u3048\u
