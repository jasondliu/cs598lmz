import codecs
# Test codecs.register_error()

import sys
try:
    str.encode
except AttributeError:
    # Python 2
    bytes = str
    byte = chr
else:
    # Python 3
    bytes = bytes
    byte = bytes

class CodecRegErrorTest(unittest.TestCase):
    def setUp(self):
        self.errors = []

    def test_register_error(self):
        self.errors = []
        codecs.register_error('test.encode', testencode)
        codecs.register_error('test.decode', testdecode)
        codecs.register_error('test.encode_surrogateescape', surrogateescapeencode)
        codecs.register_error('test.decode_surrogateescape', surrogateescapedecode)
        for encoding in ('latin-1', 'ascii', 'utf-8'):
            self.test_encode(encoding)
        for encoding in ('latin-1', 'ascii', 'utf-8'):
            self.test_decode(encoding)
