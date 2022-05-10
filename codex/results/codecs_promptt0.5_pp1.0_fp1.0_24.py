import codecs
# Test codecs.register_error
#
# Copyright (c) 2001-2003 Python Software Foundation.
# All Rights Reserved.
#
# Author: Barry Warsaw
#
# Written for 2.1.1

import unittest
from test import test_support

import codecs

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test that we can register new error handlers.
        def handler1(exception):
            return (u'', exception.end)
        def handler2(exception):
            return (u'', exception.end)
        def handler3(exception):
            return (u'', exception.end)

        codecs.register_error('test.handler1', handler1)
        codecs.register_error('test.handler2', handler2)
        codecs.register_error('test.handler3', handler3)

        self.assertEqual(codecs.lookup_error('test.handler1'), handler1)
        self.assertEqual(codecs.lookup_error('test.handler2'), handler2
