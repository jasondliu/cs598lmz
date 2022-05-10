from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 使用bz2模块的BZ2Compressor类来压缩
from bz2 import BZ2Compressor
compressor = BZ2Compressor()
compressor.compress(b'i love python')
compressor.flush()

# 压缩文件
import bz2
with bz2.open('spam.bz2', 'wt') as f:
    f.write('i love python')

# 解压文件
import bz2
with bz2.open('spam.bz2', 'rt') as f:
    print(f.read())

# 更多压缩方式
# zlib, gzip, lzma, zipfile, tarfile
