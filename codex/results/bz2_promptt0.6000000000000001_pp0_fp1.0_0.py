import bz2
# Test BZ2Decompressor with a file
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(open("sample.bz2", "rb").read())

# Test BZ2Decompressor with a string
decompressor.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

# Test BZ2Decompressor with a readable buffer
r = BytesIO(b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")
decompressor.decompress(r.read())

# Test BZ2Decompressor
