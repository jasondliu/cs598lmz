import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 如果需要对大量的数据进行压缩，使用上述模块就需要分块读取数据，压缩后再写入文件。
# 为了简化这个操作，可以使用shutil模块的make_archive()函数和unpack_archive()函数。
# 例如，下面的代码将当前目录下的
