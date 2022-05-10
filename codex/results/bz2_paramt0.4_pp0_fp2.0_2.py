from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 压缩文件
import bz2
uncompressed_data = b'Welcome to the Idiomatic Python wiki!'
with bz2.open('compressed_file.bz2', 'wt') as f:
    f.write(uncompressed_data)

# 解压文件
import bz2
with bz2.open('compressed_file.bz2', 'rt') as f:
    original_data = f.read()

# 压缩数据
import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

# 压缩文件
import
