import lzma
# Test LZMADecompressor.

def test_lzma_decompressor():
    # Test LZMADecompressor.
    #
    # This test is not exhaustive, just a sanity check.
    #
    # The test data is from the LZMA SDK (http://www.7-zip.org/sdk.html)
    #
    # The test data was compressed with the following command:
    #   lzma e -si -so testdata.bin
    #
    # The test data was decompressed with the following command:
    #   lzma d -si -so testdata.bin.lzma
    #
    # The decompressed test data was then compared to the original
    # test data.
    #
    # The test data is a 1024 byte file containing the following bytes:
    #
    #   0x00, 0x01, 0x02, ..., 0xfe, 0xff
    #
    # The compressed test data is a 13 byte file.
    #
    # The compressed test data contains the following bytes:
    #
    #   0x5d,
