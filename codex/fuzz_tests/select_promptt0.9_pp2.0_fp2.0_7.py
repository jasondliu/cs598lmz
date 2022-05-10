import select
# Test select.select for correct type and value of exception for
# empty socket set.

import select
import unittest

def raise_exception(exctype):
    raise exctype()

class ExceptionTest(unittest.TestCase):
    def test(self):
        self.assertRaises(ValueError, select.select, [], [], [], 0.0)

    def test_keyboard_interrupt(self):
        self.assertRaises((KeyboardInterrupt, SystemExit), raise_exception, KeyboardInterrupt)

if __name__ == "__main__":
    unittest.main()
