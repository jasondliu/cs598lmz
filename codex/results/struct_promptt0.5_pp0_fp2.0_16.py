import _struct
# Test _struct.Struct.__repr__()

import test.support
import unittest

class ReprTestCase(unittest.TestCase):

    def test_repr(self):
        # Issue #1626
        s = _struct.Struct('i')
        self.assertEqual(repr(s), "Struct('i')")
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.size, 4)

def test_main():
    test.support.run_unittest(ReprTestCase)

if __name__ == '__main__':
    test_main()
