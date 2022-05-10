import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.strict', handler)

# Test the handler

u = u'\u3042\u3044\u3046\u3048\u304a'

for encoding in ('iso2022_jp', 'shift_jis', 'euc_jp'):
    print '%s: %r' % (encoding, u.encode(encoding, 'test.strict'))

# Test the handler with a UnicodeEncodeError

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.strict', handler)

u = u'\u3042\u3044\u3046\u3048\u304a'

for encoding in ('iso2022_jp', 'shift_jis', 'euc_jp'):
    print '%s: %r' % (encoding, u.encode(encoding, 'test.
