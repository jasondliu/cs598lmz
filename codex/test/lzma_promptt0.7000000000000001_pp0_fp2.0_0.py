import lzma
# Test LZMADecompressor.

# The LZMA Utils can store data in a format that provides a multiple
# of 4KB blocks.  This test will not pass if the blocksize is changed.
BLOCKSIZE = 4*1024

def test():
    # Create an LZMA-compressed string.
    x = b"1234567890" * 1024
    with lzma.open(TESTFN, "wb") as lzf:
        lzf.write(x)

    # Read the LZMA-compressed file.
    with open(TESTFN, "rb") as f:
        data = f.read()

    # Decompress the string in memory.
    x2 = lzma.decompress(data)
    if x != x2:
        raise TestFailed("Decompressed data does not match original")

    # Make sure that the LZMADecompressor class doesn't choke on an
    # empty string.
    lzc = lzma.LZMADecompressor()
