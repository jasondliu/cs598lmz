from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 使用bz2压缩文件
import bz2
with open('lorem.txt', 'rb') as input:
    data = input.read()
with bz2.open('lorem.bz2', 'wb') as output:
    output.write(data)

# 压缩文件的读取
import bz2
with bz2.open('lorem.bz2', 'rb') as input:
    print(input.readline())

# 压缩文件的写入
import bz2
with bz2.open('lorem.bz2', 'wb') as output:
    output.write(b'Hello World!')

# 压缩文件的读取
import bz2
with bz2.open('lorem.bz2', 'rb') as input:
    print(input.readline())

# 压缩文
