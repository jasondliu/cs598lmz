import codecs
# Test codecs.register_error

import unittest

class CodecsModuleTest(unittest.TestCase):
    def test_register_error(self):
        # Issue #4860: register_error() must return the previous error handler
        old = codecs.register_error("strict", lambda e: ("X",e.end+1))
        new = codecs.register_error("strict", lambda e: ("Y",e.end+1))
        self.assert_(old is new)

        old = codecs.register_error("replace", lambda e: ("Z",e.end+1))
        new = codecs.register_error("replace", lambda e: ("W",e.end+1))
        self.assert_(old is not new)

        old = codecs.register_error("ignore", lambda e: ("A",e.end+1))
        new = codecs.register_error("ignore", lambda e: ("B",e.end+1))
        self.assert_(old is not new)

