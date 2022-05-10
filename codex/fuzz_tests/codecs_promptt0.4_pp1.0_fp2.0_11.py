import codecs
# Test codecs.register_error

import codecs

def test(codec, input, expected):
    try:
        codecs.lookup_error(codec)
    except LookupError:
        pass
    else:
        print "expected LookupError"
    codecs.register_error(codec, codecs.replace_errors)
    try:
        codecs.lookup_error(codec)
    except LookupError:
        print "unexpected LookupError"
    else:
        result = input.decode(codec)
        if result != expected:
            print "expected", repr(expected), "got", repr(result)

test("test", "\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e
