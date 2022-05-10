import lzma
lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
lzma.LZMACompressor(format=lzma.FORMAT_XZ)
lzma.LZMADecompressor(format=lzma.FORMAT_XZ)

# Issue #13414: Check that we can't read LZMA streams written
# by XZ Utils 5.1.xalpha or earlier.
# Unfortunately we can't create these streams ourselves.
# The following code is based on a test from the xz test suite.
# If this test fails, the specific LZMA stream used will likely
# have been fixed in liblzma.

def read_file(fn):
    with open(os.path.join(os.path.dirname(__file__), fn), "rb") as f:
        return f.read()

lzma_decompress1 = lzma.LZMADecompressor(format=l
