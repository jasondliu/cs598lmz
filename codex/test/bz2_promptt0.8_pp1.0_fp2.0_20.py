import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
compressor = bz2.BZ2Compressor()

data = "nihao\nhello\nthis is a test\n"
#compressed_data = compressor.compress(data)
