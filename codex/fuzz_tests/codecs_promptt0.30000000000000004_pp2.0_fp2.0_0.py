import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad_decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad_encode"

def bad_decode_handler(exception):
    return (u"\ufffd", exception.end)

def bad_encode_handler(exception):
    return (u"\ufffd", exception.end)

def test(input, errors='strict'):
    print "Trying to decode", repr(input)
    try:
        u = input.decode('bad_decode')
    except UnicodeError, detail:
        print "Caught", detail
    else:
        print "No exception, returned", repr(u)

    print "Trying to encode", repr(input)
    try:
        s = input.encode('bad_encode')
    except UnicodeError, detail:
        print "Caught", detail
    else:
        print "No exception, returned", repr(s
