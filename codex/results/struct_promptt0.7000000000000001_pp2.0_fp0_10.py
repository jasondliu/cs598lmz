import _struct
# Test _struct.Struct.format_map().

import unittest
from test.support import run_unittest

class FormatMapTests(unittest.TestCase):

    def test_simple(self):
        S = _struct.Struct('hhl')
        fmt = S.format_map({'h': 'i', 'l': 'q'})
        self.assertEqual(fmt, 'iiq')
        # Make sure we didn't mangle the original format
        self.assertEqual(S.format, 'hhl')

    def test_subclass(self):
        class S(_struct.Struct):
            format_map = {'h': 'i', 'l': 'q'}
        fmt = S('hhl').format
        self.assertEqual(fmt, 'iiq')

def test_main():
    run_unittest(FormatMapTests)

if __name__ == '__main__':
    test_main()
