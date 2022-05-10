import bz2
# Test BZ2Decompressor.read()

# Test different read sizes
decomp = bz2.BZ2Decompressor()
data = bz2.compress(b"foo" * 100)
for size in range(1, 600):
    got = decomp.decompress(data, size)
    expect = b"foo" * 100
    if got != expect:
        print(size, repr(got), repr(expect))
# Test BZ2Decompressor.read()

# Test readline()
decomp = bz2.BZ2Decompressor()
data = bz2.compress(b"foo\n" * 100)
got = decomp.decompress(data)
expect = b"foo\n" * 100
if got != expect:
    print(repr(got), repr(expect))
# Test BZ2Decompressor.read()

# Test readlines()
decomp = bz2.BZ2Decompressor()
data = bz2.compress(b"foo\n" * 100)
got = decomp.decompress(
