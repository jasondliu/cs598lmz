import bz2
# Test BZ2Decompressor
bz2.BZ2Decompressor().decompress('BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# Test BZ2File
bz2.BZ2File('example.bz2').read()

# Test BZ2Compressor
bz2.BZ2Compressor().compress('HelloWorld')

# Test compress/decompress
bz2.compress('HelloWorld')
bz2.decompress('BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# Test open
bz2.open('example.bz2').read()
bz
