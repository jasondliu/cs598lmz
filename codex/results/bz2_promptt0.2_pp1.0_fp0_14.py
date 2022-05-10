import bz2
# Test BZ2Decompressor

data = bz2.compress(b"this is a test")
print(data)

decompressor = bz2.BZ2Decompressor()

try:
    print(decompressor.decompress(data))
except EOFError:
    print("Cannot decompress data; data may be truncated")

decompressor.decompress(data[:-3])
decompressor.decompress(data[-3:])

print(decompressor.flush())

print(decompressor.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"))
print(decompressor.flush())

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b"BZh91AY&
