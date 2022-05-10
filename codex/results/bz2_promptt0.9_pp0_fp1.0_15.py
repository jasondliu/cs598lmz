import bz2
# Test BZ2Decompressor


class TestBZ2Decompressor:
    # Fixture setup


    @pytest.fixture(scope='class')
    def decomp(self):
        return bz2.BZ2Decompressor()


    @pytest.fixture(scope='class')
    def data(self):
        testfile = os.path.join(os.path.dirname(__file__), 'lines.bz2')
        with open(testfile, 'rb') as testf:
            return testf.read()


    def test_decompressor_attribute(self, decomp):
        # BZ2Decompressor instances should have decompressobj attribute
        with pytest.raises(AttributeError):
            decomp.decompressobj


    def test_invalid_flush_size(self, decomp):
        # Attempt to call flush() with a negative argument
        with pytest.raises(ValueError):
            decomp.flush(-1)


    def test_flush(self, decomp):
        # flush() should return an empty byte string
        # if called without having
