import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
bz2_decompressor.decompress(bz2_compressed)

# Test BZ2File
bz2_file = bz2.BZ2File('file.bz2')
bz2_file.read()
bz2_file.close()

# Test BZ2Compressor
bz2_compressor = bz2.BZ2Compressor()
bz2_compressor.compress(b'hello world!')
bz2_compressor.flush()

# Test open
bz2.open('file.bz2')
bz2.open('file.bz2', mode='wt')
bz2.open('file.bz2', mode='wt', compresslevel=9)
bz2.open('file.bz2', mode='rb')

# Test compress
bz2.compress(b'hello world!')
bz2.compress(b'hello world!', compresslevel=9)


