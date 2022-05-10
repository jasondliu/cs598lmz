import lzma
# Test LZMADecompressor
#
# The LZMA file format is described in
# http://en.wikipedia.org/wiki/Lzma#File_format

def test_lzma_format():
    # Create a compressed stream
    compressed = []
    c = lzma.LZMADecompressor()
    for i in range(100):
        compressed.append(c.compress(b"hello"))
    compressed.append(c.flush())

    # Create a file with a bogus lzma header
    f = io.BytesIO()
    f.write(b"BOGUS")
    f.write(b"".join(compressed))
    f.seek(0)

    # Test various header sizes
    for i in range(len(b"BOGUS")):
        f.seek(i)
        try:
            lzma.LZMADecompressor().decompress(f.read())
        except ValueError:
            pass
        else:
            self.fail("didn't raise ValueError")

    # Test the correct header
