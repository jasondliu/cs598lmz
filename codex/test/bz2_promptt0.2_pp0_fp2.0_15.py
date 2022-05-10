import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()

try:
    decompressed = decompressor.decompress(data)
except Exception as err:
    print('Error:', err)
else:
    print('Output is {} bytes'.format(len(decompressed)))
    print(decompressed)

print('Still {} bytes of compressed data left'.format(len(decompressor.unused_data)))

decompressor = bz2.BZ2Decompressor()

