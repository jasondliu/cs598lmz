import bz2
# Test BZ2Decompressor
assert bz2.decompress(bz2.compress(b'\x00' * 128 * 1024 * 1024)) == b'\x00' * 128 * 1024 * 1024
# Test LZMACompressor
assert lzma.LZMADecompressor().decompress(lzma.LZMACompressor().compress(b'\x00' * 128 * 1024 * 1024)) == b'\x00' * 128 * 1024 * 1024

bz2_compressor = bz2.BZ2Compressor()
lzma_compressor = lzma.LZMACompressor()

# Do some CPU-bound work to warm up caches and CPU before benchmarking
bz2_compressor.compress(b'\x00' * 128 * 1024 * 1024)
lzma_compressor.compress(b'\x00' * 128 * 1024 * 1024)

bz2_compress_time = timer(lambda: bz2_compressor.compress(b'\x00' * 128 * 1024 * 1024))
lzma_compress
