import lzma
# Test LZMADecompressor

# Test LZMADecompressor

def test_LZMADecompressor_1():
    # Test LZMADecompressor
    #
    # This test checks that LZMADecompressor works when fed one byte at a time.
    #
    # The test data is the first 4K from the Silesia compression corpus.
    # http://sun.aei.polsl.pl/~sdeor/index.php?page=silesia
    #
    # The data is compressed with lzma at compression level 1.
    #
    # The test data was generated with the following command:
    #
    #     dd if=silesia.tar bs=1k count=4 | lzma -1 | xxd -i
    #
    # The resulting data was embedded in this test.
    #
    # The test data is the first 4K from the Silesia compression corpus.
    # http://sun.aei.polsl.pl/~sdeor/index.php?page=silesia
    #
    # The
