import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() 和 bz2.decompress() 函数分别对数据压缩和解压缩

# 压缩文件
with open('file.txt', 'rb') as input:
    data = input.read()
with bz2.BZ2File('file.txt.bz2', 'wb') as output:
    output.write(data)

# 解压缩文件
with bz2.BZ2File('file.txt.bz2', 'rb') as input:
    data = input.read()
with open('file.txt', 'wb') as output:
    output.write(data)

# 压缩文件和解压缩文件的操作方式和 gzip 模块
