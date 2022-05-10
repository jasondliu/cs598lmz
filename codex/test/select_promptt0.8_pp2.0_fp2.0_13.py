import select
# Test select.select() with some non-valid parameters
# TODO For some reason this test is skipped under FreeBSD (bug?)
# It passes when run manually, though...
#import unittest

class SelectTest(unittest.TestCase):
    def test_error_conditions(self):
        # Try select() with invalid arguments
        self.assertRaises(ValueError, select.select, [], [], [], -1)

        # Illegal FDs
        self.assertRaises(ValueError, select.select, [-1], [], [])
        self.assertRaises(ValueError, select.select, [-1, -2], [], [])
        self.assertRaises(ValueError, select.select, [-1, -2, -3], [], [])

        # Try select() with a bad file descriptor
        # Create a socket and then close it.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.close()
