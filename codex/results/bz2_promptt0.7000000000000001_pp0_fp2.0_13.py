import bz2
# Test BZ2Decompressor as above, with BZ2Compressor as a context manager.
decomp = bz2.BZ2Decompressor()
with bz2.BZ2Compressor(9) as comp:
    comp.compress(b"abc")
    comp.flush()
    print(decomp.decompress(comp.compress(b"def")))

# Test BZ2Compressor as a context manager with an alternative compresslevel.
with bz2.BZ2Compressor(5) as comp:
    comp.compress(b"abc")
    comp.flush()
    print(decomp.decompress(comp.compress(b"def")))

# Test BZ2Compressor as a context manager without an initializer.
with bz2.BZ2Compressor() as comp:
    comp.compress(b"abc")
    comp.flush()
    print(decomp.decompress(comp.compress(b"def")))


# Test BZ2Decompressor with input and output buffers.
buf_in = b"x" * 1000
