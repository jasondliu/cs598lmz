import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() 和 bz2.decompress() 函数分别对一个字符串进行压缩和解压缩。
# 如果要压缩的数据量很大，可以使用 BZ2File 对象来代替。
# 下面是一个将一个文件压缩后再解压缩的例子：

import bz2
with open('example.txt', 'rb') as input:
    with bz2.BZ2File('example.txt.bz2', 'wb') as output:
        output.writelines(input)

with bz2.BZ2File('example.txt.bz2', '
