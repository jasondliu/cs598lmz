import codecs
# Test codecs.register_error()

from test import test_support
import unittest

# test_support.verbose = 1

class CodecsRegisterErrorTest(unittest.TestCase):

    def test_lookup_error(self):
        # Testing the 'lookup_error' argument
        #
        # First, look up a non-existing handler
        self.assertRaises(LookupError, codecs.lookup_error, '__spam__')

        # Then, register a handler for the '__spam__' error
        def __spam__(message):
            return (u'\ufffd', len(message))
        codecs.register_error('__spam__', __spam__)

        # And look it up again
        t, f, s = codecs.lookup_error('__spam__')
        self.assertEqual(t, __spam__)
        self.assertEqual(s, None)

        # Now, register another handler for the '__spam__' error
        def __spam__(message):
            return (u'
