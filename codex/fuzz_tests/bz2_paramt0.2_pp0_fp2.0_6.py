from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 内存中的解压
import bz2
uncompressed_data = b''
decompressor = bz2.BZ2Decompressor()
for chunk in iter(lambda: f.read(100 * 1024), b''):
    uncompressed_data += decompressor.decompress(chunk)

# 压缩数据
import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

# 压缩文件
import bz2
with open('file.txt', 'rb') as input:
    with bz2.open('file.txt.bz2', 'wb') as output
