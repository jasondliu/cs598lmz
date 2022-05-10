from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')

# print(type(BZ2Decompressor.decompress))
# from bz2 import BZ2Decompressor
# decompressor = BZ2Decompressor()
# decompressor.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
# decompressor.flush()
print(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'.decode('utf-8'))
