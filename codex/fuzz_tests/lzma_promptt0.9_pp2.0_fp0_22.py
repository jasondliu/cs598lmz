import lzma
# Test LZMADecompressor interface

from test.test_support import findfile, run_unittest, import_module

test_support = import_module('test.test_support')

# Start of testdata
magic1 = '\xfd7zXZ\x00'          # first 6 bytes of every .xz file
empty = '<empty file>'

class LZMADecompressorTestCase(unittest.TestCase):

    def test_decompress_nonstreaming(self):
        # Read everything into memory at once
        with open(findfile('xzdata.xz'), 'rb') as f:
            data = f.read()
        self.assertTrue(data.startswith(magic1), repr(data[:6]))
        with lzma.LZMADecompressor() as de:
            self.assertGreater(len(data), 10)
            self.assertEqual(de.decompress(data), empty)
            self.assertEqual(de.decompress(bytes()), bytes())
            self.assertRaises(IO
