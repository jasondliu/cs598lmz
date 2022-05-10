from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 读取bz2文件
with open('hello.txt.bz2', 'rb') as f:
    data = BZ2Decompressor().decompress(f.read())
    print(data)

# 压缩文件
with open('hello.txt', 'rb') as input:
    with BZ2File('hello.txt.bz2', 'wb') as output:
        copyfileobj(input, output)

# 解压文件
with BZ2File('hello.txt.bz2', 'rb') as input:
    with open('hello.txt', 'wb') as output:
        copyfileobj(input, output)

# 更高级的压缩方式
import bz2
bz2.compress(b'hello world!')

# 压缩率较高的压缩
data = open('lorem.txt',
