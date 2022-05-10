import codecs
# Test codecs.register_error

# This test is used to check that codecs.register_error() works as expected.
# It is not a test of the codecs module itself.

import codecs
import encodings

def test_register_error():
    # Test that the error handler is called.
    #
    # We use the 'replace' error handler, which replaces the unencodable
    # character with a '?' character.
    #
    # First, we encode a character which is not in the encoding's character
    # set.  Then, we encode a character which is in the encoding's character
    # set.  In both cases, we check that the error handler is called.
    #
    # If the error handler is not called, then the encode() method will
    # raise a UnicodeEncodeError exception.
    #
    # Note that the 'replace' error handler is the default error handler for
    # most encodings.  However, we explicitly specify it here to make sure
    # that the error handler is called.
    #
    # Note that we use the 'strict' error handler when encoding the
