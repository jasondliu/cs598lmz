import bz2
# Test BZ2Decompressor
assert bz2.decompress(bz2.compress(b'\x00' * 128 * 1024 * 1024)) == b'\x00' * 128 * 1024 * 1024
# Test LZMACompressor
