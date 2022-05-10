from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# 如果你想给一个文件对象添加压缩或者解压缩的功能，可以使用内置的 io.TextIOWrapper() 函数。
# 下面是一个交互式会话，展示了如何将一个文本文件压缩后再解压缩：
import bz2
f = open('file.txt', 'wt')
f.write('Contents go here')
f.close()

f2 = bz2.open('file.bz2', 'wt')
f2.write(f.read())
f2.close()

f3 = bz2.open('file.bz2', '
