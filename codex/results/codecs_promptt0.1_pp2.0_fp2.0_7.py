import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test_decode(encoding):
    try:
        u = '\xff'.decode(encoding, 'test.bad_decode')
    except UnicodeError:
        pass
    else:
        print 'no exception'

def test_encode(encoding):
    try:
        '\xff'.encode(encoding, 'test.bad_encode')
    except UnicodeError:
        pass
    else:
        print 'no exception'

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test_decode(encoding)
    test_encode(encoding)

# Test codecs
