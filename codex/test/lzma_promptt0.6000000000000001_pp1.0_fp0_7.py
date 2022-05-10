import lzma
# Test LZMADecompressor class
#
# Run with pytest
#
# $ pytest
#
# To see verbose output
#
# $ pytest -v
#
# For a single test
#
# $ pytest test_lzma.py::test_lzma_1
#
# To see the output of the test
#
# $ pytest -s test_lzma.py::test_lzma_1


# Test an empty file
def test_lzma_1():
    d = lzma.LZMADecompressor()
    assert d.decompress(b'') == b''
    assert d.unused_data == b''


# Test a simple file
def test_lzma_2():
    d = lzma.LZMADecompressor()
