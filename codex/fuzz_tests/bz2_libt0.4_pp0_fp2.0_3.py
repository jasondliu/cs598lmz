import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
import bz2
with open('file.txt', 'rb') as input:
    with bz2.open('file.txt.bz2', 'wb') as output:
        output.write(input.read())

# 解压文件
import bz2
with bz2.open('file.txt.bz2', 'rb') as input:
    with open('file.txt', 'wb') as output:
        output.write(input.read())
