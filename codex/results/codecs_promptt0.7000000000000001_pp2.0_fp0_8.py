import codecs
# Test codecs.register_error
from test.test_support import run_unittest

import encodings
from encodings import utf_8

from StringIO import StringIO

class CodecRegistryErrorTest(unittest.TestCase):

    def setUp(self):
        self.errors = []
        self.encode = lambda input, errors: (input, errors)
        self.decode = lambda input, errors: (input, errors)
        self.incrementalencoder = self.incrementaldecoder = None

    def test_register_error_noncallable(self):
        # registering something that is not callable should raise TypeError
        for error in [1, '', u'']:
            self.assertRaises(TypeError, codecs.register_error, error)

    def test_stderr_handler(self):
        codecs.register_error('stderr', codecs.stderr_error_handler)
        stream = StringIO()
        handler = codecs.lookup_error('stderr')
        handler(u'\ufffd', u'\
