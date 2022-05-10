import bz2
# Test BZ2Decompressor.__init__ and decompress()
for args in [(), (15000,), (16384,)]:
    compress = bz2.BZ2Compressor()
    compressobj = bz2.BZ2Compressor(*args)
    # The tests below test a dummy decompressobj, not the
    # decompress() function. However, we're testing the compress()
    # function as a side-effect.
    uncompress = bz2.decompress(compress.flush())
    assert len(uncompress) == 10240
    assert (compressobj.compress(uncompress) +
        compressobj.flush() == bz2.compress(uncompress))

# Test the max_length parameter to BZ2Decompressor.decompress().
d = bz2.BZ2Decompressor()
assert d.decompress(bz2.compress(b'hello there'), 0) == b''
assert d.unused_data == b''
assert d.decompress(bz2.compress(b'hello there')) ==
