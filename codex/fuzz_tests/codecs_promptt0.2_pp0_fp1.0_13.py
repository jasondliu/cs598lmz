import codecs
# Test codecs.register_error()

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    elif isinstance(exc, UnicodeEncodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('my_replace', my_replace)

def test(encoding):
    print '-'*20, encoding
    print 'encode:', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding, 'my_replace'))
    print 'decode:', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding).decode(encoding, 'my_replace'))

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test(enc
