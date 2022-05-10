import bz2
# Test BZ2Decompressor.__init__ by passing input string
decompress = bz2.BZ2Decompressor()
i = decompress.decompress(b"BZh91AY&SY")
if i != b"Hello world!":
    raise TestFailed("bug in BZ2Decompressor.__init__")

# Test BZ2Decompressor.decompress by passing input string
decompress = bz2.BZ2Decompressor()
i = decompress.decompress(b"BZh91AY&SY\x00\x00\x00\x01\x0a\x00\x00\x00\x04")
if i != b"Hello world!":
    raise TestFailed("bug in BZ2Decompressor.decompress")

# Test BZ2Decompressor.decompress by passing input file object
infile = io.BytesIO(b"BZh91AY&SY\x00\x00\x00\x01\x0a\x00\x00\x00\x04")
decompress
