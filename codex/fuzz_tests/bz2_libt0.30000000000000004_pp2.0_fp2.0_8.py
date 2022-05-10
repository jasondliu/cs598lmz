import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# bz2.compress() 和 bz2.decompress() 函数同样支持大型数据块的压缩和解压缩。
# 下面是一个例子，展示了如何将一个文件中的数据块压缩后写入另一个文件：

import bz2
with open('example.txt', 'rb') as input:
    with bz2.open('example.txt.bz2', 'wb') as output:
        output.write(input.read())

# 另一个例子，展示了如何将一个大型文件压缩
