import bz2
# Test BZ2Decompressor.decompress()

# Test decompressing normal data
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(bz2.compress(b"test")) == b"test"

# Test decompressing empty string
