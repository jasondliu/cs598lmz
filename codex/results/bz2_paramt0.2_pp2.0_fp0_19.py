from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# 如果你想使用压缩数据流的方式来处理大量的数据，可以使用 BZ2File() 函数。
# 下面是一个将一个文件压缩后再解压的例子：
import bz2
with open('lorem.txt', 'rb') as input:
    with bz2.open('lorem.bz2', 'wb') as output:
        output.writelines(input)
with bz2.open('lorem.bz2', 'rb') as input:
    with open('lorem_copy.txt', 'wb') as output:
        for line in input:
            output.write(line)

# 在上面的代码中，使用 open
