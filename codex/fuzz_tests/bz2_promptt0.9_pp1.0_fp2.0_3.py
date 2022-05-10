import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()
result = decomp.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
result += decomp.decompress('h\x9e\x84\x1dy\x8a\xbbLP\x91\xf08')
print(result)

# Test BZ2File
bzfile = bz2.BZ2File(filename)
print(bzfile.read())
bzfile.close()

# Test bz2
print(bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3
