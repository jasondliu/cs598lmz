from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(raw_compressed_data)
# 'This is the original text.'

# 将一个文件压缩后放到另一个文件中
import bz2
with open('/Users/michael/example.txt', 'rb') as input:
    with bz2.open('/Users/michael/example.bz2', 'wb') as output:
        output.write(input.read())

with bz2.open('/Users/michael/example.bz2', 'rb') as input:
    with open('/Users/michael/example.txt', 'wb') as output:
        output.write(input.read())


# 可以直接使用上下文管理器的方式来操作压缩文件
from bz2 import BZ2File
with BZ2File('/Users/michael/example.bz2', 'rb')
