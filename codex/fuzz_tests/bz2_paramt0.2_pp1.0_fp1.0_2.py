from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# bz2.BZ2Compressor
# bz2.BZ2Decompressor

# bz2.compress(data, compresslevel=9)
# bz2.decompress(data)

# bz2.open(filename, mode='r', compresslevel=9)
# bz2.open(filename, mode='w', compresslevel=9)
# bz2.open(filename, mode='x', compresslevel=9)
# bz2.open(filename, mode='a', compresslevel=9)

# bz2.open(filename, mode='rb', compresslevel=9)
# bz2.open(filename, mode='wb', compresslevel=9)
# bz2.open(filename, mode='xb', compresslevel=9)
# bz2.open(filename, mode='ab', compresslevel=9)

# bz2.open(filename, mode='rt', compresslevel=9)
# bz2.open(filename, mode
