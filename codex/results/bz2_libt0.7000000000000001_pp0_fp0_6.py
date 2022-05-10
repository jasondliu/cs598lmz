import bz2
bz2.decompress(data)

# 从data解压缩数据
bz2.decompress(data)

# 从文件末尾读取数据
with open('somefile.txt', 'rb') as f:
    f.seek(-100, 2)
    d = f.read(100)

# 使用seek()来寻找文件末尾对齐的偏移量
f = open('somefile.txt', 'rb')
f.seek(-1, 2)
f.tell()

# 在不支持seek()的文件中读取数据，比如网络流
from functools import partial
RECORD_SIZE = 32
with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
