import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# Test BZ2File
bz2.BZ2File(filename)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(b'hello world')
compressor.flush()

# Test BZ2File
bz2.BZ2File(filename)
