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
        u"abc".encode(encoding)
    except UnicodeError:
        pass
    else:
        print 'no exception raised'

def test_encode(encoding):
    try:
        u"abc".encode(encoding)
    except UnicodeError:
        pass
    else:
        print 'no exception raised'

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test_decode(encoding + '_test.bad_decode')
    test_encode(encoding + '_test.bad_encode')
