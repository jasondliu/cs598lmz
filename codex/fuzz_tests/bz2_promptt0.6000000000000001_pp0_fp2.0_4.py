import bz2
# Test BZ2Decompressor.flush()

data = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
c = bz2.BZ2Decompressor()

# Decompress data
result = c.decompress(data)
print(result.decode("ascii"))

# Decompress rest of the stream
result += c.flush()
print(result.decode("ascii"))
