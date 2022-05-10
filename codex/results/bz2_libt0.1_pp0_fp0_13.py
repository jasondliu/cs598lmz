import bz2
bz2.decompress(bz2_data)

# bz2.BZ2File
bz2_file = bz2.BZ2File('example.bz2')
print(bz2_file.read())
bz2_file.close()

# bz2.open
with bz2.open('example.bz2', 'rt') as bz2_file:
    print(bz2_file.read())

# bz2.compress
data = b'Lots of data here.'
len(data)
compressed = bz2.compress(data)
len(compressed)

# bz2.decompress
original = bz2.decompress(compressed)
len(original)

# bz2.compresslevel
for i in range(10):
    print(i, len(bz2.compress(data, compresslevel=i)))

# bz2.decompress
bz2.decompress(b'BZh91AY&SYA\xaf\x82
