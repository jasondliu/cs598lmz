import codecs
# Test codecs.register_error

import codecs

def raise_exc(exc):
    raise exc

def strict_decode(input, errors='strict'):
    return codecs.charmap_decode(input, errors, {ord(c): c for c in 'abc'})

def strict_encode(input, errors='strict'):
    return codecs.charmap_encode(input, errors, {ord(c): c for c in 'abc'})

