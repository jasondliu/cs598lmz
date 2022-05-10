import bz2
# Test BZ2Decompressor
decompressor = BZ2Decompressor()
data = decompressor.decompress(bz2_data)
data

# Test BZ2File
with BZ2File(bz2_file, 'rb') as bz2_file:
    bz2_file.read()

# Test BZ2Compressor
compressor = BZ2Compressor()
compressor.compress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
compressor.flush()
