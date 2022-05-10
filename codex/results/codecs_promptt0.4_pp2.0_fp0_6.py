import codecs
# Test codecs.register_error

import codecs
import unittest

# Test the error handlers and the name registration

class TestCodecs(unittest.TestCase):

    def test_register_error(self):
        # test codecs.register_error
        #
        # First, we get the standard error handler for strict encoding
        # and decoding.
        strict = codecs.lookup_error('strict')
        #
        # Now, we define a new error handler that will be used instead
        # of 'strict'
        def my_error_handler(exception):
            return (u'', exception.end)
        #
        # Register it under the name 'my_error_handler'
        codecs.register_error('my_error_handler', my_error_handler)
        #
        # Now, we can get the error handler we registered
        my_error_handler = codecs.lookup_error('my_error_handler')
        #
        # And we can use it for encoding and decoding
        self.assertEqual(
            'abc'.decode('asci
