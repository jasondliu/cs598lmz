import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()
decomp.decompress(bz2_data)

import gzip
# Test GzipDecompressor
decomp = gzip.GzipDecompressor()
decomp.decompress(gzip_data)

import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
decomp.decompress(lzma_data)

import zlib
# Test ZlibDecompressor
decomp = zlib.decompressobj()
decomp.decompress(zlib_data)

import lz4
# Test LZ4Decompressor
decomp = lz4.frame.LZ4FrameDecompressor()
decomp.decompress(lz4_data)

import zstandard
# Test ZstdDecompressor
decomp = zstandard.ZstdDecompressor()
decomp.decompress(zstd_data)


# Test BZ2Compressor, LZMACompressor, Gzip
