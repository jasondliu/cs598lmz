import bz2
# Test BZ2Decompressor

with bz2.BZ2Decompressor() as dec:
    print(dec.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))

# Test BZ2Compressor

with bz2.BZ2Compressor() as comp:
    print(comp.compress(b'hello'))
    print(comp.flush())

# Test compress()

print(bz2.compress(b'hello'))
print(bz2.compress(b'hello'))

# Test decompress()

print(bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9
