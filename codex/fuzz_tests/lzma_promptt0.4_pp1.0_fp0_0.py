import lzma
# Test LZMADecompressor

# Test LZMADecompressor

def test_LZMADecompressor():
    # Test LZMADecompressor
    #
    # This test comes from the LZMA SDK (C) Igor Pavlov
    # http://www.7-zip.org/sdk.html
    #
    # The input data was compressed using the command-line version of LZMA
    # with the following options:
    #     lzma e -d23 data.bin data.lzma
    #
    # The data was then decompressed using the command-line version of LZMA
    # with the following options:
    #     lzma d data.lzma data.bin
    #
    # The resulting data.bin file was then compared to the original data.bin
    # file to ensure that the two were identical.
    #
    # The compressed data was then extracted from the resulting data.lzma file
    # and pasted into the test_data_compressed variable below.
    test_data_compressed = \
        b'\x5d
