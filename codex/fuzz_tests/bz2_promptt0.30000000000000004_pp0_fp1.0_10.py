import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes long'.format(len(data)))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print('Output is {} bytes long'.format(len(result)))
print(result)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
result = compressor.compress(b'Hello World!')
result += compressor.flush()
print(result)

# Test BZ2File
with bz2.open('lorem.txt.bz2', 'rt') as input:
    print(input.read())

with bz2.open('lorem.txt.bz2', 'wt
