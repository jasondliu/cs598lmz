import codecs
# Test codecs.register_error()

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'', exc.end)
    elif isinstance(exc, UnicodeEncodeError):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('my_replace', my_replace)

def test_decode(encoding):
    print '-', encoding
    try:
        u = '\xff'.decode(encoding, 'my_replace')
    except UnicodeDecodeError:
        print 'UnicodeDecodeError'
    else:
        print repr(u)

def test_encode(encoding):
    print '-', encoding
    try:
        s = u'\xff'.encode(encoding, 'my_replace')
    except UnicodeEncodeError:
        print 'UnicodeEncodeError'
    else:
        print repr(s)

test_decode('as
