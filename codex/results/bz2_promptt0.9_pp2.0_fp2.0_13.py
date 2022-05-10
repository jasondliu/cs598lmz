import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

d = bz2.BZ2Decompressor()

print('# Feed uncompressed data')
print(d.decompress(data))
print()
print('# Feed again the uncompressed data')
print(d.decompress(data))

# BZ2File

with bz2.BZ2File('file.bz2', 'rb') as f:
    print(f.read())

with open('file.bz2', 'rb') as f:
    print(bz2.decompress(f.read()))

# BZ2Decompress

print(bz2.decompress(data))
print(bz2.decompress(data, 3
