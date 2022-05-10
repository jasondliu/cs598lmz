import codecs
# Test codecs.register_error

def bad_decode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad', bad_decode)

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad', bad_encode)

def bad_streamreader(stream, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad', bad_streamreader)

def bad_streamwriter(stream, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad', bad_streamwriter)

def bad_streamreaderwriter(stream, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad', bad_streamreaderwriter)

def bad_streamrecoder(stream, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad', bad_streamrecoder)

print('TESTS BEGIN')

