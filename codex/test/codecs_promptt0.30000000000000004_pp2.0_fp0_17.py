import codecs
# Test codecs.register_error()

import codecs

def my_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        x, y = exc.object[exc.start:exc.end], exc.end
        print('error', x, y, exc.end)
        return (u'', exc.end+1)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('test.myerror', my_error)

def test(encoding):
    print('\nTESTING', encoding, '\n')
    s = '\xe4\xf6\xfc'
    print('ORIG  :', s)
    s2 = s.decode(encoding, 'test.myerror')
    print('DECODED:', s2)
    s3 = s2.encode(encoding)
    print('ENCODED:', s3)

for encoding in ('latin-1', 'iso-8859-1', 'iso-8859-15'):
    test
