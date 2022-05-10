import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(len(data))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
print(decompressor.decompress(data))

print(decompressor.unused_data)

# Decompress with one shot
print(bz2.decompress(data))

# Compress with one shot
print(bz2.compress(b"this is the string to compress"))

# Compress/Decompress files
with bz2.open('file.bz2', 'wt') as f:
    f.write("this is the string to compress")

with bz2.open('file.bz2', 'rt
