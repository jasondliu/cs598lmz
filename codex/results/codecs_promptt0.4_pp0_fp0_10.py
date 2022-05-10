import codecs
# Test codecs.register_error
#
# This test is part of the test suite for the codecs module.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
#

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):

        # Test the register_error API

        # Test 1: registering a new error handler
        def test_handler(exception):
            return (u'[%s]' % exception.object, exception.end)
        codecs.register_error('test.handler', test_handler)
        self.assertEqual(codecs.lookup_error('test.handler'), test_handler)

        # Test 2: registering an error handler under a name that's
        # already used
        def test_handler2(exception):
            return (u'[%s]' % exception.object, exception.end)
        codecs.register_error('test.handler', test_handler2)
