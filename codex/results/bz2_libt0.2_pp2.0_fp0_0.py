import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() 和 bz2.decompress() 函数分别对应压缩和解压缩。
# 压缩后的数据就可以保存到文件或者通过网络传输了。

# 压缩文件
import bz2
with open('lorem.txt', 'rb') as input:
    with bz2.open('lorem.bz2', 'wb') as output:
        output.writelines(input)

# 解压文件
import bz2
with bz2.open('lorem.bz2', 'rb') as input:
    with open('lorem.txt', 'wb') as output:
        output.writelines(input)

# 压缩
