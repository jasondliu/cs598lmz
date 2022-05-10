import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# Test BZ2File
f = bz2.open("file.bz2", mode='wt')
f.write("some data")
f.close()
