import lzma
# Test LZMADecompressor, LZMAEncoder, FrameFormat and FrameInfo objects
# Note that the LZMA codec is only available if the lzma module from PEP 3198
# is available.
#
LZMA_FORMATS = [
    (FrameFormat.RAW, raw_lzma_decompress, raw_lzma_compress),
    (FrameFormat.XZ, lzma_decompress, lzma_compress),
    (FrameFormat.AUTO, lzma_decompress, lzma_compress)]
LZMA_EXTRA = {'filters': [{'id': lzma.FILTER_LZMA1,
    'dict_size': 8 * 1024 * 1024,
    'lc': 3,
    'lp': 0,
    'pb': 2,
    'mode': lzma.MODE_NORMAL}]}
LZMA_CANARY = b"The quick brown fox jumps over the lazy dog."
LZMA_PADDED_CANARY = b"The quick brown fox jumps over the lazy dog.\x00\x00
