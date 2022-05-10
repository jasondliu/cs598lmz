import codecs
# Test codecs.register_error()
# See also test_codecs.py
#
# This test needs to be executed in a separate process because
# it needs to register a new codec error handler.
#
# Test for issue #1558: codecs.register_error() doesn't work
# with 'replace' and 'xmlcharrefreplace'

import sys
import unittest
from test import test_support
import codecs

# The error handler should be able to handle unicode arguments
class TestUnicodeReplace(unittest.TestCase):

    def test_unicode_replace(self):
        def unicode_replace(exc):
            if not isinstance(exc, UnicodeEncodeError):
                raise TypeError("don't know how to handle %r" % exc)
            return (u'', exc.end)
        codecs.register_error('test.unicode_replace', unicode_replace)
        self.assertEqual(u'abc\uffff\u0100'.encode('ascii', 'test.unicode_replace'),
                         'abc')

    def test_xmlcharref
