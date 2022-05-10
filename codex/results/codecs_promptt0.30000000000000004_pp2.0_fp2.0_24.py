import codecs
# Test codecs.register_error()

def bad_decode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.lookup', bad_decode)

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.encode', bad_encode)

def bad_recursive_decode(input, errors='strict'):
    return codecs.charmap_encode(input, errors, {0xFFFE: 0xFFFE})

codecs.register_error('test.recursive', bad_recursive_decode)

def bad_recursive_encode(input, errors='strict'):
    return codecs.charmap_decode(input, errors, {0xFFFE: 0xFFFE})

codecs.register_error('test.recursive_encode', bad_recursive_encode)

def bad_ignore_decode(input, errors='strict'):
    return (u"\uFFFE",
