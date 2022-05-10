import codecs
# Test codecs.register_error
# test register_error, unregister_error

def encode(input, errors=None):
    return ("testencoder", len(input)), len(input)

def decode(input, errors=None):
    return ("testdecoder", len(input)), len(input)

