from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# 使用 bz2 压缩数据
import bz2
for line in open('/etc/passwd', 'rt'):
    print(line, end='')

compressed = bz2.compress(b'a very long string that we want to compress')
print(compressed)
print(bz2.decompress(compressed))

# bz2 压缩文件
bz2.compress(b'a very long string that we want to compress')
bz2.decompress(compressed)

# bz2 压缩文件
with open('filename.txt.bz2', 'wt') as f:
    f.write('Contents of the example file go here.\n')
with open('filename.txt.bz2', 'rt') as f:
    print(f.read())

import bz2
with open('/etc/passwd', 'rb') as f:
    compressed = bz
