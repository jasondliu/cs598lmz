import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError("bad decode")

def bad_encode(input, errors='strict'):
    raise UnicodeError("bad encode")

codecs.register_error("test.bad_decode", bad_decode)
codecs.register_error("test.bad_encode", bad_encode)

def test(input, errors="strict"):
    print "Trying to encode", repr(input), "with errors =", errors
    try:
        print "Encoding:", repr(input.encode("ascii", errors))
    except UnicodeError, detail:
        print "UnicodeError:", detail
    print "Trying to decode", repr(input), "with errors =", errors
    try:
        print "Decoding:", repr(input.decode("ascii", errors))
    except UnicodeError, detail:
        print "UnicodeError:", detail

test("abc")
test("\x80")
test("\x
