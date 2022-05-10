import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error("test.bad_decode", bad_decode)
codecs.register_error("test.bad_encode", bad_encode)

def test(input, errors='strict'):
    print "Trying to encode", repr(input), "with error handling", errors
    try:
        x = input.encode("ascii", errors)
    except UnicodeError, detail:
        print "UnicodeError:", detail
    else:
        print "Result:", repr(x)
    print
    print "Trying to decode", repr(input), "with error handling", errors
    try:
        x = input.decode("ascii", errors)
    except UnicodeError, detail:
        print "UnicodeError:", detail
    else:
        print "Result:
