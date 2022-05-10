import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()
decomp.decompress(comp.compress(b"hello world"))

# Test BZ2Compressor
comp = bz2.BZ2Compressor()
comp.compress(b"hello ")
comp.compress(b"world")
comp.flush()

# Test BufferedReader
bz2.BZ2File(bufio.BufferedReader(io.BytesIO(b"hello")))

# Test BZ2File
bz2.BZ2File("/tmp/foo.bz2", "w")

# Test BZ2File
bz2.BZ2File(io.BytesIO(b"hello"))

# Test open
bz2.open("/tmp/foo.bz2", "w")

# Test open
bz2.open(io.BytesIO(b"hello"))
