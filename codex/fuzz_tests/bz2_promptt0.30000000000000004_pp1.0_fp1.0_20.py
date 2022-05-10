import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(len(data))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print(result)
print(len(result))

# Test BZ2File
with bz2.open('example.bz2', 'wt') as f:
    f.write('Contents of the example file go here.\n')

with bz2.open('example.bz2', 'rt') as f:
    data = f.read()
    print(data)

# Compressing and Decompressing Data in Memory
data = b'Contents of the example file go here.\n' * 100000
len(data)

compressed = bz2
