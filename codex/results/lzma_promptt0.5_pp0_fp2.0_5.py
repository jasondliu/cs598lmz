import lzma
# Test LZMADecompressor with a single-byte input.
# This test is designed to catch the bug fixed in issue #13983.
class TestLZMADecompressorSingleByteInput(unittest.TestCase):

    def test_single_byte_input(self):
        self.assertEqual(b'', lzma.LZMADecompressor().decompress(b'\x00'))


if __name__ == '__main__':
    unittest.main()
