import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()
try:
    print(decompressor.decompress(data))
except Exception as e:
    print(e)

print('Leftover is {} bytes'.format(len(decompressor.unused_data)))

# Test BZ2File

bz_file = bz2.BZ2File('lorem.txt.bz2')
print(bz_file.read().decode('utf-8'))
bz_file.seek(0)
print(bz_file.readline().decode('utf-8'))
