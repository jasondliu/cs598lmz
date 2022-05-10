import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# Test BZ2File
import bz2
with bz2.BZ2File('archive.bz2', 'w') as output:
  with open('big_file', 'rb') as input:
    output.write(input.read())

# Test BZ2Compressor
import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'Hello World!')

# Test BZ2Decompressor.decompress
import bz2
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SY\x94$|\
