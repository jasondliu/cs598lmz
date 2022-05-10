import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

for encoding in ('ascii', 'latin-1', 'utf-8'):
    print '%s:' % encoding
    try:
        u'\u1234'.encode(encoding, 'test.bad_encode')
    except UnicodeError:
        print '  encode: UnicodeError'
    else:
        print '  encode: no error'
    try:
        '\xff'.decode(encoding, 'test.bad_decode')
    except UnicodeError:
        print '  decode: UnicodeError'
    else:
        print '  decode: no error'

# Test codecs.lookup

import codecs

def test_lookup(enc
