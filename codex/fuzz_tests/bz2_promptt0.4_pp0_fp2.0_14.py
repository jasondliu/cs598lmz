import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()

try:
    result = decompressor.decompress(data)
except Exception as e:
    print('Error:', e)
else:
    print('Output is {} bytes'.format(len(result)))
    print(result)

print('Regaining the original:', data == decompressor.decompress(compressed))

print('Total input length:', len(data))
print('Total output length:', decompressor.eof)

decompressor = bz2.BZ2Decompressor()
for block in blocks:
    print(decompressor.decompress(block
