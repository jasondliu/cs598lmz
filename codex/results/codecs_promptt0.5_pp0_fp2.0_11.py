import codecs
# Test codecs.register_error()

# This test is a bit tricky because we have to generate an error
# message that is encoded in a codec that doesn't exist.  So we
# have to create a fake codec that raises an error on encode()
# and register it.

import codecs
import test.test_support

class BadEncode(object):
    def encode(self, input, errors='strict'):
        raise UnicodeEncodeError('fake codec', u'', 0, 1, "ouch")

codecs.register(BadEncode)

# Create an error message that is encoded in the fake codec
def badfunc():
    raise UnicodeEncodeError('fake codec', u'', 0, 1, "ouch")

class BadEncodeTest(unittest.TestCase):
    def test_bad_encode(self):
        try:
            badfunc()
        except UnicodeEncodeError, exc:
            s = str(exc)
    def test_bad_encode_str(self):
        # Issue #1733
        try:
            badfunc()
        except UnicodeEncodeError
