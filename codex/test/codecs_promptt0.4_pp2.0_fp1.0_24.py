import codecs
# Test codecs.register_error()
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# $Id: test_register_error.py,v 1.1.1.1 2006/05/30 06:01:19 hhzhou Exp $

import unittest

class RegisterErrorTestCase(unittest.TestCase):

    def test_register_error(self):

        # Test whether the error handlers are properly registered
        # and used by the codecs module.

        import codecs
        from codecs import lookup
        from test import test_support

        class X:
            def __init__(self):
                self.called = 0
                self.errors = []
            def __call__(self, errors):
                self.called = self.called + 1
                self.errors.append(errors)
                return (u'', 0)

        x = X()
        codecs.register_error('test.x', x)

        # Lookup the error handler
