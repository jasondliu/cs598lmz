import lzma
lzma.open

import pytest # type: ignore

# When single-sourceing, pytest is perhaps not available
# So we invent a skip mechanism here
try:
    skip = pytest.mark.skip(reason="Don't have lzma")
except NameError:
    def skip(param):
        return lambda func: func

@skip(pytest.mark.skipif(not lzma, reason="Don't have lzma"))
def test_compression_decompression():
    compression_template = "files/{compressor}/compression.out"
    decompression_template = "files/{compressor}/decompression.in"
    compressor_name = "xz"
    inset = "Hello World!"
    compressor = lzma.LZMACompressor()
    with open(compression_template, mode="wb") as compressed:
        compressed.write(compressor.compress(inset.encode("utf8")))
        compressed.write(compressor.flush())

    decompressor = lzma.LZMADecompressor
