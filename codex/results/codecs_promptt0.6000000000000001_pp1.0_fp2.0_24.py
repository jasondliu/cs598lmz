import codecs
# Test codecs.register_error
#
# $Id: codecs_register_error.py,v 1.1.1.1 2001/08/09 20:39:00 kjetilja Exp $

import unittest

class RegisterErrorTestCase(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error
        encoder = codecs.getencoder('latin-1')
        decoder = codecs.getdecoder('latin-1')
        def bad_handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.bad', bad_handler)
        self.assertEqual(
            encoder('\xa0\xa1\xa2', 'test.bad'),
            (u'\xa0\xa1\xa2', 3)
        )
        self.assertEqual(
            decoder('\xc0\xc1\xc2', 'test.bad'),
            (u'\ufffd\ufffd\ufffd', 3)
        )

    def test_
