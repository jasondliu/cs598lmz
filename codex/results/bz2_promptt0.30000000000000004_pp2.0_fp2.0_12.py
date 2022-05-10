import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Test BZ2File
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(b'hello world')

with bz2.BZ2File('file.bz2', 'rb') as f:
    print(f.read())

# Test compress
bz2.compress(b'hello world')

# Test decompress
bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x
