import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xd0\x04\xe8\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(bz2.decompress(data))

print(bz2.decompress(data[0:4]))

print(bz2.decompress(data[4:10]))

print(bz2.decompress(data[10:22]))

print(bz2.decompress(data[22:]))

print(bz2.decompress(data[4:4]))

print(bz2.decompress(data[4:4], 0))

print(bz2.decompress(data[4:4], 1))

print(bz2.decompress(data[4:4], 1, 10))

print(bz2.decompress(data[
