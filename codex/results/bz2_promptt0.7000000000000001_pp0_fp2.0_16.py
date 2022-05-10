import bz2
# Test BZ2Decompressor on an uncompressed string

obj = bz2.BZ2Decompressor()
obj.decompress('BZh91AY&SY.\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Test BZ2Decompressor on a compressed string

obj2 = bz2.BZ2Decompressor()
obj2.decompress(obj.decompress('BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'))

# Test BZ2Decompressor with a file

uncompressed_data = 'The same line, over and over.\n'
compressed_
