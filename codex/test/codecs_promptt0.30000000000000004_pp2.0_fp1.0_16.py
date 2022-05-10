import codecs
# Test codecs.register_error()

def bad_decode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_encode', bad_encode)

def bad_encode2(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_encode2', bad_encode2)

def bad_encode3(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_encode3', bad_encode3)

def bad_encode4(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_encode4', bad_encode4)

def bad_encode5(input, errors='strict'):
    raise UnicodeError

