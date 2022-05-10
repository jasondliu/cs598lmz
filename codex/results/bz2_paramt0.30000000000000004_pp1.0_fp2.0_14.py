from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.open()
with bz2.open('sample.bz2', 'rt') as bz2_file:
    print(bz2_file.readline())

# bz2.compress()
original_data = b'This is the original text.'
print(len(original_data))
bz2_data = bz2.compress(original_data)
print(len(bz2_data))

# bz2.decompress()
bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(bz2.decompress(bz2_data))

# bz2.BZ2Compressor()
original_data = b'This is
