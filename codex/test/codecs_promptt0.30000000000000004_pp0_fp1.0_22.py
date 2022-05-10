import codecs
# Test codecs.register_error

import codecs

def raise_exc(exc):
    raise exc

def bad_encode(input, errors='strict'):
    raise_exc(UnicodeEncodeError("bad_encode", u"", 0, 1, "ouch"))

def bad_decode(input, errors='strict'):
    raise_exc(UnicodeDecodeError("bad_decode", "", 0, 1, "ouch"))

def bad_recursive_encode(input, errors='strict'):
    return bad_encode(input, errors)

def bad_recursive_decode(input, errors='strict'):
    return bad_decode(input, errors)

def bad_recursive_call(input, errors='strict'):
    return codecs.charmap_encode(input, errors)

def bad_ignore_encode(input, errors='strict'):
    return (u"", len(input))

