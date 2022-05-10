from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# 如果你想使用压缩数据流的方式来处理大量的数据，可以使用 BZ2Compressor 和 BZ2Decompressor 对象。
# 下面是一个压缩文件的例子：
import bz2

with open('lorem.txt', 'rb') as input:
    with bz2.open('lorem.bz2', 'wb') as output:
        output.writelines(input)

# 如果你想压缩的文件很大，那么你可以分块的方式来处理：
import bz2

with open('lorem.txt', 'rb') as input:
