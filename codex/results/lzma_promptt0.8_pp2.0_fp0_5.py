import lzma
# Test LZMADecompressor, etc.
import lzma
import os

def test_bad_filters():
    for filters in [
        [],
        [{"id": lzma.FILTER_X86}],
        [{"id": lzma.FILTER_DELTA}],
        [{"id": lzma.FILTER_X86}, {"id": lzma.FILTER_DELTA}],
        [{"id": lzma.FILTER_X86}, {"id": lzma.FILTER_DELTA, "dist": 2}],
        [{"id": lzma.FILTER_X86}, {"id": lzma.FILTER_DELTA, "dist": 2}],
        [{"id": lzma.FILTER_LZMA2, "dictsize": 16384},
         {"id": lzma.FILTER_DELTA, "dist": 2}],
    ]:
        comp = lzma.LZMACompressor(filters=filters)
        assert comp.compress(b"") == b""
       
