import bz2
# Test BZ2Decompressor

d = bz2.BZ2Decompressor()

# Decompress the data
data = d.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
print data

# Decompress the data with a max length
data = d.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084', 100)
print data

# Decompress the data with a max length
data = d.decompress('BZh91AY&SYA\xaf\x82\r
