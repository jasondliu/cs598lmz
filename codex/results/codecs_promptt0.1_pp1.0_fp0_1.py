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
        u = unicode('abc', encoding)
    except UnicodeError:
        pass
    else:
        raise AssertionError, 'decoding did not fail'

def test_encode(encoding):
    try:
        s = u'abc'.encode(encoding)
    except UnicodeError:
        pass
    else:
        raise AssertionError, 'encoding did not fail'

test_decode('test.bad_decode')
test_encode('test.bad_encode')

# Test codecs.lookup

import codecs

def test(encoding):
    try:

