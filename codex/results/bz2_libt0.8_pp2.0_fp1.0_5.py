import bz2
bz2.decompress(bz2_data)
bz2_data = b'BZh91AY&SY.\xc8N\x18\x00\x00\x00\x01\x00\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
bz2.decompress(bz2_data)

# example of bad data
#x = bz2.BZ2Decompressor().decompress(bz2_data)
#print(x.decode())


import gzip
with gzip.open('example.txt.gz', 'rt') as f:
    text = f.read()
    print(text)

with gzip.open('example.txt.gz', 'wt') as f:
    f.write
