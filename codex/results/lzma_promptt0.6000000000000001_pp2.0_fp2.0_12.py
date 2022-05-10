import lzma
# Test LZMADecompressor objects

from io import BytesIO

from test import support
from test.support import TESTFN, run_unittest
from test.support import bigmemtest, bigaddrspacetest

class BaseTest(object):
    def check_valid_data(self, data, compressor=None):
        if compressor is None:
            compressor = self.lzma_module.LZMACompressor()
        # Use the default settings (preset=6)
        compressed = compressor.compress(data)
        compressed += compressor.flush()
        self.check_compress_decompress_equal(data, compressed)

    def check_invalid_data(self, data, compressor=None):
        if compressor is None:
            compressor = self.lzma_module.LZMACompressor()
        # Use the default settings (preset=6)
        self.assertRaises(self.lzma_module.LZMAError, compressor.compress,
                          data)

    def check_valid_fileobj(self, data, compressor=None):
        if compressor is None
