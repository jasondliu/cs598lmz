import codecs
# Test codecs.register_error()

import codecs

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('test.replace', replace_error)

def test(encoding):
    print '-'*50
    print 'Encoding:', encoding
    print 'encode():', repr(u'\u3042\u3044\u3046'.encode(encoding, 'test.replace'))
    print 'decode():', repr(u'\u3042\u3044\u3046'.encode(encoding).decode(encoding, 'test.replace'))

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32']:
    test(encoding)

print '-'*50
print 'Encoding:', 'iso2022_jp'
print 'encode():', repr(
