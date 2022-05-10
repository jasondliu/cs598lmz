import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 如果需要对大量的数据进行压缩，使用上述代码就很麻烦了。
# 可以使用 zlib.compress() 和 zlib.decompress() 函数来代替。
# 下面是一个例子：

s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

# 压缩效率比较
