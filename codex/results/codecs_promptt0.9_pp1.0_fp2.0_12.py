import codecs
# Test codecs.register_error() with illegal name
try:
    codecs.register_error('öäü', 'strict')
except ValueError:
    pass
else:
    raise Exception("Didn't raise ValueError")
# Try a different style of name
class IllegalCodecException(Exception):
    pass

codecs.register_error('illegal_codec', IllegalCodecException)

class UTest(codecs.UnicodeTranslateError):
    pass

codecs.register_error('utest', UTest)
#
msg = "non-ASCII character '\N{MICRO SIGN}'"
test_input = u'abcd\N{MICRO SIGN}xyz'

class Test:

    def test_strict(self):
        self.check_exception('iso8859-1', test_input, 'strict',
                             UnicodeEncodeError, msg)

    def test_replace(self):
        result = test_input.encode('iso8859-1', 'replace')
        assert result == 'abcd?xyz', 'result should be
