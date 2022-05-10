from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b"Hello World"))

# bz2.BZ2File
# bz2.BZ2File(filename[, mode[, buffering[, compresslevel]]])
# mode: r, w, x, a
# buffering: 0, 1, 2, ...
# compresslevel: 1, 2, 3, ..., 9

# bz2.open
# bz2.open(filename[, mode[, compresslevel]])
# mode: r, w, x, a
# compresslevel: 1, 2, 3, ..., 9

# bz2.compress
# bz2.compress(data[, compresslevel])
# compresslevel: 1, 2, 3, ..., 9

# bz2.decompress
# bz2.decompress(data)

# bz2.BZ2Compressor
# bz2.BZ2Compressor([compresslevel])
# compresslevel: 1, 2, 3, ..., 9

# bz2.BZ2Decompressor
