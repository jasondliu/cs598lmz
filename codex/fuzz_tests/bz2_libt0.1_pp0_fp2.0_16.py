import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 如果需要对大量的数据进行压缩，使用上述模块就需要分块读写。
# 为了简化这个操作，可以使用 zlib.compress() 和 zlib.decompress() 函数。
# 它们能够处理大的数据流并且不会将所有的压缩数据放到内存中。

# 压缩
