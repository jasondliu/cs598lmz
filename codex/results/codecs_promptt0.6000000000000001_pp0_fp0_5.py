import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        self.assertTrue(issubclass(codecs.LookupError, LookupError))
        self.assertTrue(issubclass(codecs.CodecRegistryError, LookupError))
        self.assertTrue(issubclass(codecs.CodecError, UnicodeError))
        self.assertTrue(issubclass(codecs.StreamReaderError, UnicodeError))
        self.assertTrue(issubclass(codecs.StreamWriterError, UnicodeError))
        self.assertTrue(issubclass(codecs.ReaderError, UnicodeError))
        self.assertTrue(issubclass(codecs.WriterError, UnicodeError))
        self.assertTrue(issubclass(codecs.IncrementalEncoderError, UnicodeError))
        self.assertTrue(issubclass(codecs.IncrementalDecoderError, UnicodeError))
        self.assertTrue(issubclass(codecs.
