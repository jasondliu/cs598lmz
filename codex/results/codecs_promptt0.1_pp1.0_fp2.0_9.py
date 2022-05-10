import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test_decode():
    # Test decoding
    for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
        try:
            u = unicode('abc', encoding, 'test.bad_decode')
        except UnicodeError:
            pass
        else:
            print 'Expected error did not occur for', encoding

def test_encode():
    # Test encoding
    for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
        try:
            s = u'abc'.encode(encoding, 'test.bad_encode')
        except UnicodeError:
            pass

