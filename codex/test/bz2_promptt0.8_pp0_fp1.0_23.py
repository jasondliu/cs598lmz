import bz2
# Test BZ2Decompressor.__init__ by passing input string
decompress = bz2.BZ2Decompressor()
i = decompress.decompress(b"BZh91AY&SY")
