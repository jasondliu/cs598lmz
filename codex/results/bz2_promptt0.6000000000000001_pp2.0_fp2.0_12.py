import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print('Output is {} bytes'.format(len(result)))
print(result)

print('Total input is {} bytes'.format(len(data) + decompressor.eof_byte_offset))
print('Total output is {} bytes'.format(len(result) + decompressor.unused_data))
# Test BZ2File
with bz2.open('lorem.txt.bz2') as input:
    print(input.read())
import gzip
import shutil
with open('lorem.txt', 'rb') as input:

