import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_encode', bad_encode)

def bad_encode_errorhandler(exception):
    raise UnicodeError

def bad_decode_errorhandler(exception):
    raise UnicodeError

def test(encoding):
    print '-'*50
    print 'Encoding', encoding
    try:
        u'\u3042'.encode(encoding, 'test.bad_encode')
    except UnicodeError:
        print 'UnicodeError raised as expected'
    else:
        print 'ERROR: UnicodeError not raised'
    try:
        u'\u3042'.encode(encoding, 'test.bad_encode_errorhandler')
    except UnicodeError:
        print 'Unicode
