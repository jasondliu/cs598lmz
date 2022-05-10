from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'Hello World'))

# bz2.BZ2Compressor
# bz2.BZ2Decompressor

# bz2.compress(data, compresslevel=9)
# bz2.decompress(data)

# bz2.open(filename, mode='r', compresslevel=9)
# bz2.open(filename, mode='w', compresslevel=9)
# bz2.open(filename, mode='x', compresslevel=9)

# bz2.open(filename, mode='rb')
# bz2.open(filename, mode='wb')
# bz2.open(filename, mode='xb')

# bz2.open(filename, mode='rt')
# bz2.open(filename, mode='wt')
# bz2.open(filename, mode='xt')

# bz2.open(filename, mode='rU')
# bz2.open(filename, mode='wU')
# bz2.open(filename,
