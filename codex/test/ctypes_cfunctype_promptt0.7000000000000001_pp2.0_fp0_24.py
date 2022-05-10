import ctypes
# Test ctypes.CFUNCTYPE() function
#
# NOTE: This is not a test case, but rather a utility to help
#       determine the correct calling conventions for various platforms
#
# See tests/test_issue_13664.py for a test case
#
# To run this program, simply execute this file directly. The output
# will be written to a file named 'test_issue_13664.out'
#
# You can then examine this file to see the results of the tests.

class platform:
    def is64bit(self):
        return sys.maxsize > 2**32
    def is32bit(self):
        return sys.maxsize <= 2**32

class issue_13664:
    def __init__(self):
        self.platform = platform()
        self.incorrect = 0
    def test(self):
        if self.platform.is64bit():
            self.test_64bit()
        else:
            self.test_32bit()
        self.write_results()
    def test_32bit(self):
        self.test_cdecl()
        self.test
