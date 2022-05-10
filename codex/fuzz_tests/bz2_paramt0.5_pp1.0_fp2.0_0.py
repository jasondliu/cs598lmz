from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world'))

# 使用压缩文件
# 可以使用内置的bz2模块来读取一个bz2压缩文件，也可以使用bz2.BZ2File类来像普通文件那样读取一个bz2压缩文件
import bz2
with bz2.open('file.bz2', 'rt') as f:
    text = f.read()

# 如果要让bz2模块创建一个压缩文件，你需要使用open()函数并传入一个以'w'或'wb'模
