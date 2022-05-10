from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 使用压缩文件
import bz2
uncompress = bz2.BZ2Decompressor()
with open('somefile.bz2', 'rb') as f:
    for data in iter(lambda: f.read(100 * 1024), b''):
        r = uncompress.decompress(data)
        if r:
            print(r)

# 压缩文件的操作
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

with bz2.open('somefile.bz2', 'rt') as f:
    print(f.read())

# 压缩数据
import bz2
data = b'Lots of data here'
compressed = bz2.compress(data)
print(compressed)

# 解压数据
import bz2

