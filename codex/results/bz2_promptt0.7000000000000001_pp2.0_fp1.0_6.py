import bz2
# Test BZ2Decompressor.copy()

class TestCopy(unittest.TestCase):
    def test_copy(self):
        data = b"foo"
        comp = bz2.BZ2Compressor()
        uncomp = bz2.BZ2Decompressor()

        # Try compressing the entire data in one go
        comp_data = comp.compress(data)
        comp_data += comp.flush()

        # Try compressing the data using copy
        uncomp_copy = uncomp.copy()
        self.assertEqual(uncomp_copy.unused_data, b"")
        self.assertEqual(uncomp_copy.unconsumed_tail, b"")
        self.assertEqual(uncomp_copy.eof, 0)
        self.assertEqual(uncomp_copy.needs_input, 1)
        decomp = uncomp.decompress(comp_data)
        self.assertEqual(decomp, data)
        self.assertEqual(uncomp.unused_data, b"")
        self.assertEqual(uncomp.uncons
