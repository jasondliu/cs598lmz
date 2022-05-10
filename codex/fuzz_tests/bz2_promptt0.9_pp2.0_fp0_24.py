import bz2
# Test BZ2Decompressor class. 
# Reference: https://docs.python.org/2/library/bz2.html
class TestDecompressor(unittest.TestCase):
    """
    Test the BZ2Decompressor class.
    """

    def setUp(self):
        """
        Create a BZ2Decompressor object.
        """
        self.bz_obj = bz2.BZ2Decompressor()

        # Create a bz2 file containing a short string.
        self.fname = 'test.bz2'
        self.data = "This is a test message."
        f = bz2.BZ2File(self.fname, "w")
        f.write(self.data)
        f.close()


    def test_decompressed(self):
        """
        Test data returned by the bz2_obj.decompress() method.
        """
        with open(self.fname, "rb") as f:
            data_decompressed = self.bz_obj.decompress(f.read())
