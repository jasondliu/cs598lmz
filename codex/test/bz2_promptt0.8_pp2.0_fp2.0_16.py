import bz2
# Test BZ2Decompressor.

decompressor = bz2.BZ2Decompressor()

for p in [b"", b"a", b"abc", b"hello world"]:
    for block in [p, p * 100]:
        for flush in [True, False]:
            print("flush", flush, "block size", len(block))
            compressed = bz2.compress(block, compresslevel=9)
