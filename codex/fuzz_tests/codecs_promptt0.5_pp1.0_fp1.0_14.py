import codecs
# Test codecs.register_error
#
# Copyright (C) 2002-2003 Python Software Foundation; All Rights Reserved

import codecs
import unittest
import test.test_support

class CodecTest(unittest.TestCase):
    def test_register_error(self):
        def my_error_handler(exception):
            return (u"", exception.end)

        def my_error_handler2(exception):
            return (u"", exception.end+1)

        def my_error_handler3(exception):
            raise UnicodeError, "test"

        # first, test that the default error handler works
        self.assertEqual(u"abc\ufffe\u0123\ufffe\u4567\ufffe",
                         u"abc\x80\u0123\x80\u4567\x80".decode("charmap",
                                                               "ignore"))

        # register a new error handler
        codecs.register_error("test.my_error_handler", my_error_handler)

        # now, test that the new error handler works
        self
