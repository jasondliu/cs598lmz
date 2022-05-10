import codecs
# Test codecs.register_error()

# Test registering the same handler multiple times

import codecs

def handler(exception):
    return (u"XXX", exception.end)

def test(name):
    codecs.register_error(name, handler)
    codecs.register_error(name, handler)
    codecs.register_error(name, handler)
    codecs.register_error(name, handler)
    # Check that it's actually registered
    return codecs.lookup_error(name) is handler

