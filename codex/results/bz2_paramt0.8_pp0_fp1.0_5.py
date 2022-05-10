from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(f.read())

with bz2.BZ2File('largefile.bz2') as f:
    for line in f:
        print(line)

import bz2
bz2.decompress(bz2_data)

# 打开一个gzip或bz2格式的压缩文件，并且不需要先解压缩到磁盘
import gzip
with gzip.open('file.gz', 'rt') as f:
    text = f.read()

with bz2.open('file.bz2', 'rt') as f:
    text = f.read()

# 性能应用
# 采用二进制数组来存储非图像数据
import array
nums = array.array('i', [1, 2, 3, 4])

