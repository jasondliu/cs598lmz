import codecs
# Test codecs.register_error()

def bad_decode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_encode', bad_encode)

def bad_encode_with_reason(input, errors='strict'):
    raise UnicodeError("reason")

codecs.register_error('test.bad_encode_with_reason', bad_encode_with_reason)

def bad_encode_with_reason_and_object(input, errors='strict'):
    raise UnicodeError("reason", input, 42, 43)

codecs.register_error('test.bad_encode_with_reason_and_object', bad_encode_with_reason_and_object)

class BadDecode:
    def __init__(self, errors='strict'):
        pass
