import codecs
# Test codecs.register_error
import sys
import test_support
import unittest

class TestCodecs(unittest.TestCase):

    def test_readbuffer(self):
        import StringIO
        # This test should not raise UnicodeDecodeError, see issue #2960
        '\x80\x80\x80'.decode('utf-8', 'ignore')
        '\x80\x80\x80'.decode('utf-8', 'replace')
        '\x80\x80\x80'.decode('utf-8', 'backslashreplace')
        '\x80\x80\x80'.decode('utf-8', 'xmlcharrefreplace')
        self.assertEqual('\x80\x80\x80'.decode('utf-8', 'strict'), u'\udc80\udc80\udc80')

    def test_register_error(self):
        # this test should not raise UnicodeDecodeError
        import codecs
        def bad_decode1(input, errors='strict'):
            raise ValueError
       
