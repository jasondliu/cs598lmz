import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

decompressor = bz2.BZ2Decompressor()

print(decompressor.decompress(data))

print(decompressor.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'))

print(decompressor.unused_data)

try:
    decompressor.decompress(b'x\x9c')
except IOError as e:
    print("Error:", e)

decompressor = bz2.BZ2Decompressor()

print(decompressor.decompress(data))

print(decompressor.decompress(b
