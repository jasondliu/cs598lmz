import bz2
# Test BZ2Decompressor.decompress()
cdata = bz2.compress(b"hello world")
bzdec = bz2.BZ2Decompressor()
decompressed_data = bzdec.decompress(cdata)
decompressed_data

