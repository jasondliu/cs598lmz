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

