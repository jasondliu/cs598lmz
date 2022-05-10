import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

# test bad_decode
for errors in ('test.bad_decode', 'test.bad_decode', 'test.bad_decode'):
    try:
        u'\xff'.encode('ascii', errors)
    except UnicodeError, exc:
        if str(exc) != "bad decode":
            raise RuntimeError, "wrong exception"
    else:
        raise RuntimeError, "no exception"

# test bad_encode
for errors in ('test.bad_encode', 'test.bad_encode', 'test.bad_encode'):
    try:
        u'\u20ac'.encode('as
