from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 这里的LZMADecompressor类是一个可用于流式解压缩的对象，可以像一个文件那样使用它。
# 下面是一个使用这个类的例子：

import lzma

with lzma.open('foo.xz', 'rt') as f:
    text = f.read()

# 如果你想控制压缩级别，可以传递一个preset参数给LZMA类。
# 下面是一个使用preset=9的例子：

import lzma

with lzma.open('foo.xz', 'wt', preset=
