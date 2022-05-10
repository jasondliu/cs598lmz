from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

#The bz2 module contains a BZ2Decompressor class which, when fed bytes, decompresses them into bytes

# bz2.decompress(data)
#The decompress() function accepts the data to decompress in bytes and returns the decompressed data in bytes

bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2.decompress(bz2_data)

#The bz2 module provides a complete implementation of the bzip2 compression format.

# bz2.compress(data)
#The compress() function accepts the data to compress in bytes and returns the compressed data in bytes

original_data = b'This is the original text.'
print(len(original_data))
b
