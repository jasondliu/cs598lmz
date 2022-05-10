import bz2
# Test BZ2Decompressor
bz2_comp = bz2.BZ2Compressor()
bz2_decomp = bz2.BZ2Decompressor()
bz2_comp.compress(b"Hello World!")

bz2_comp.flush()

bz2_decomp.decompress(b"BZh91AY&SY\x94\x8c\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BA\x06\xbe\x084")

bz2_decomp.decompress(b"BZh91AY&SY\x94\x8c\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BA\x06\xbe\x084")
bz2_decomp.decompress(b"BZh91AY&SY\x94\x
