import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeDecodeError("bad", input, 0, 1, "bad")

def bad_encode(input, errors='strict'):
    raise UnicodeEncodeError("bad", input, 0, 1, "bad")

codecs.register_error("test.bad_decode", bad_decode)
codecs.register_error("test.bad_encode", bad_encode)

def test(name, input, errors, expected):
    print name,
    try:
        result = codecs.decode(input, errors)
    except UnicodeError, e:
        result = str(e)
    if result != expected:
        print "ERROR:", repr(result), "!=", repr(expected)
    else:
        print "OK"

test("strict", "abc\xff", "strict",
     "UnicodeDecodeError: 'ascii' codec can't decode byte 0xff in position 3: ordinal not in range(128
