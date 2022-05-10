import codecs
# Test codecs.register_error
import sys
from test import support
from test.support import TESTFN, findfile

class CodecRegistryTestCase(unittest.TestCase):
    encoding = 'junk-register-error'

    def setUp(self):
        self.errors = []
        self.handler = lambda name: self.errors.append(name)

    def test_register_error(self):
        # Register an error handler, then unregister it
        codecs.register_error(self.encoding, self.handler)
        try:
            codecs.lookup_error(self.encoding)
        finally:
            codecs.register_error(self.encoding, None)

    def test_lookup_error(self):
        # Register an error handler, then look it up
        codecs.register_error(self.encoding, self.handler)
        try:
            handler = codecs.lookup_error(self.encoding)
            self.assertEqual(handler, self.handler)
        finally:
            codecs.register_error(self.encoding, None
