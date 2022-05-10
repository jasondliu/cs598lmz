import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)

import sys
if sys.platform == 'win32':
    import msvcrt
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

import unittest
from test import support

class Test_StreamReaderWriter(unittest.TestCase):

    def test_streamwriter(self):
        f = codecs.getwriter('utf-16')(BytesIO())
        self.assertEqual(f.encoding, 'utf-16')
        self.assertEqual(f.errors, 'strict')
        self.assertFalse(f.line_buffering)
        self.assertEqual(f.write('abc'), 6)
        self.assertEqual(f.write('def'), 6)
        self.assertEqual(f.write(''), 0)
        self.assertEqual
