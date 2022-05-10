import codecs
# Test codecs.register_error
#
# This is a test for the register_error function in the codecs module.
# The test will succeed if no exceptions are raised.

class CodecTestError(Exception):
    pass

def ETFCodecTest(str):
    raise CodecTestError

# For each codec, the last codec in the list of codecs is chosen for
# the encoding.
codecs.register_error('test.codec', ETFCodecTest)

def test(data):
    print "Trying to encode: %r" % data
    try:
        data.encode('ascii', 'test.codec')
    except CodecTestError:
        print "CodecTestError raised!"
    except UnicodeEncodeError:
        print "UnicodeError raised!"

test(u"This is a test")
test(u"\u3042")
