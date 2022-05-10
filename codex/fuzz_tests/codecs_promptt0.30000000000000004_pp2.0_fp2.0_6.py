import codecs
# Test codecs.register_error

import codecs
import unittest

class TestCodecs(unittest.TestCase):

    def test_register_error(self):
        def replace_errors(exc):
            if isinstance(exc, UnicodeDecodeError):
                return (u'\ufffd', exc.end)
            elif isinstance(exc, UnicodeEncodeError):
                return (u'\ufffd', exc.end)
            else:
                raise TypeError("don't know how to handle %r" % exc)

        codecs.register_error('test.replace', replace_errors)
        self.assertEqual(codecs.lookup_error('test.replace'), replace_errors)

        self.assertEqual(u'abc'.encode('ascii', 'test.replace'), 'abc')
        self.assertEqual(u'\u1234'.encode('ascii', 'test.replace'), '\ufffd')
        self.assertEqual(u'\u1234'.encode('ascii', 'test.replace'), '\ufffd')
