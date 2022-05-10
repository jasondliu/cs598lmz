import bz2
# Test BZ2Decompressor:
# - decompress some bytes
# - return unused_data
# - feed empty bytes
d = bz2.BZ2Decompressor()
