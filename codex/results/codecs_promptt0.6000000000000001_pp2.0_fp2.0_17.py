import codecs
# Test codecs.register_error()

import codecs
import sys

# test the 'strict' error handler

def test(codec, input, expected):
    try:
        result = codecs.decode(input, codec)
    except UnicodeError, exc:
        if str(exc) == expected:
            print "OK, got expected exception", expected
        else:
            print "ERROR: unexpected exception", exc
    else:
        print "ERROR: expected exception not raised:", expected

print 'TESTING STRICT'

test('utf-8', '\x80',
     "'utf8' codec can't decode byte 0x80 in position 0: "
     "invalid start byte")

test('utf-8', '\xc0\x80',
     "'utf8' codec can't decode bytes in position 0-1: "
     "invalid continuation byte")

test('utf-8', '\xc0\x80\xc0\x80',
     "'utf8' codec can't decode bytes in position 0-1: "
     "invalid continuation byte")

test('utf
