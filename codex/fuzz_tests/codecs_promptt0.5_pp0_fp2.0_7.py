import codecs
# Test codecs.register_error

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        x = u''.join(unichr(0xfffd) for c in exc.object[exc.start:exc.end])
        return (x, exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("test.replace", my_replace)

def test(encoding):
    print '-'*20, encoding
    s = 'pi: \u03c0'
    print 'INPUT:', s
    try:
        u = s.decode(encoding)
    except UnicodeDecodeError, e:
        print 'ERROR:', e
        u = s.decode(encoding, 'test.replace')
    print 'OUTPUT:', u

test('ascii')
test('latin-1')
test('utf-8')
test('utf-16')
