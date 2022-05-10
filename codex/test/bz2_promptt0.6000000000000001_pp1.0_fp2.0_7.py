import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes long'.format(len(data)))

decompressor = bz2.BZ2Decompressor()

try:
    decompressed = decompressor.decompress(data)
    print('Output is {} bytes long'.format(len(decompressed)))
    print(decompressed)
except Exception as e:
    print('Error:', e)

print('Regenerating the compressed data and decompressing it:', end=' ')
try:
    recompressed = decompressor.compress(decompressed) + decompressor.flush()
except Exception as e:
    print('Error:', e)
else:
    print('OK')
