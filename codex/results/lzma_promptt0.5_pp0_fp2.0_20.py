import lzma
# Test LZMADecompressor
from lzma.tests.support import TESTFN, unlink
from lzma.tests.support import run_unittest, import_module

# Skip this test if the _lzma module isn't available.
lzma = import_module('lzma')

def roundtrip(data, mode='simple', format=lzma.FORMAT_XZ,
              check=-1, preset=None, filters=None):
    # Encode the data.
    compressor = lzma.LZMACompressor(format=format, check=check,
                                     preset=preset, filters=filters)
    encoded = compressor.compress(data) + compressor.flush()

    # Decode the data.
    decoded = lzma.decompress(encoded)

    # Check that the roundtrip was successful.
    assert decoded == data, (len(decoded), len(data))

class LZMADecompressorTestCase(unittest.TestCase):
    def test_decompress(self):
        # Test a simple roundtrip.
       
