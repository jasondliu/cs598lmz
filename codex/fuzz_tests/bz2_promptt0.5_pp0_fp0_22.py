import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(len(data))

decompressor = BZ2Decompressor()
print(decompressor.decompress(data))
print(decompressor.flush())

decompressor = BZ2Decompressor()
print(decompressor.decompress(data[:-1]))
try:
    decompressor.flush()
except EOFError as err:
    print('ERROR:', err)

decompressor = BZ2Decompressor()
print(decompressor.decompress(data[:-5]))
try:
    decompressor.flush()
except EOFError as err:
    print('ERROR:', err)

decompressor = BZ2Decompressor()
print(
