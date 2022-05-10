import bz2
# Test BZ2Decompressor.

decompressor = bz2.BZ2Decompressor()

for p in [b"", b"a", b"abc", b"hello world"]:
    for block in [p, p * 100]:
        for flush in [True, False]:
            print("flush", flush, "block size", len(block))
            compressed = bz2.compress(block, compresslevel=9)
            decompressed = decompressor.decompress(compressed,
                                                   flush=flush)
            print("Unused data:", decompressor.unused_data)
            print("decompressed", decompressed)
            assert decompressed == block

compressed = bz2.compress(b"abc", compresslevel=9)
for i in range(len(compressed)):
    decompressed = decompressor.decompress(compressed[:i])
    print("Unused data:", decompressor.unused_data)
    if decompressed:
        print("decompressed", decompressed)
    assert decompressed == b""

decompressor.decomp
