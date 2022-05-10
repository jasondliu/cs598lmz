import codecs
# Test codecs.register_error()

# This is a test for the codecs module.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# *** Ensure that test runs with the current locale setting ***

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):

        # Test registering of new error handlers
        def handler1(exception):
            return ('x', exception.start + 1)

        codecs.register_error('test1', handler1)
        self.assertEqual(codecs.lookup_error('test1'), handler1)

        def handler2(exception):
            return ('xx', exception.start + 2)

        codecs.register_error('test2', handler2)
        self.assertEqual(codecs.lookup_error('test2'), handler2)

        # Check that registering twice fails
        self.assertRaises(ValueError, codecs.register_error
