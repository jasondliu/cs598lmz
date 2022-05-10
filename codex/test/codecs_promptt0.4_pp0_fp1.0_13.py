import codecs
# Test codecs.register_error()

def bad_decode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_encode', bad_encode)

def bad_encode_errorhandler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test.bad_encode_errorhandler', bad_encode_errorhandler)

def bad_recursive_errorhandler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test.bad_recursive_errorhandler', bad_recursive_errorhandler)

def bad_recursive_decode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_recursive_decode', bad_recursive_decode)

