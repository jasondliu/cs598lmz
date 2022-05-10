import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()
decomp.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

# Test BZ2Compressor
comp = bz2.BZ2Compressor()
comp.compress(b"this is a test")
comp.flush()

# Test BZ2File
with bz2.BZ2File("test.bz2", "w") as f:
    f.write(b"this is a test")

with bz2.BZ2File("test.bz2", "r") as f:
    f.read()

# Test BZ2File with a context manager
with bz2.BZ2File("test.bz2", "w") as f:
    f
