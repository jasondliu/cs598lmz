import codecs
# Test codecs.register_error()
def bad_decode(input, errors='strict'):
    raise TypeError("bad_decode")
codecs.register_error('test.bad_decode', bad_decode)
