import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding != 'test.searchfunction':
        return None
    return codecs.CodecInfo(
        name='test.searchfunction',
        encode=lambda input, errors: (input.encode('ascii'), len(input)),
        decode=lambda input, errors: (input.decode('ascii'), len(input)),
    )

codecs.register(search_function)

# Register an error handler
def replace_error(error):
    if not isinstance(error, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % error)
    return (u'\ufffd', error.end)
codecs.register_error('test.replace', replace_error)

# Encode
