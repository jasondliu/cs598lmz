from lzma import LZMADecompressor
LZMADecompressor(16*1024).decompress(b'...')
# b'...'

# 如果你想将一个大文件压缩成一个单独的压缩文件，可以使用一个像 gzip 或 bz2 模块那样的高级封
# 装器。下面是一个使用 LZMA 算法的例子：

import lzma
with lzma.open('foo.xz','wt') as f:
    f.write('Hello World')
# 如果需要压缩更高级的文件格式，比如 ZIP 文件，可以使用 zipfile 模块。
# 该模
