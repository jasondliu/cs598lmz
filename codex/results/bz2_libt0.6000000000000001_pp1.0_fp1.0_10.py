import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2的压缩效率比zlib高，但是是非常小的文件，而且压缩和解压的速度相对较慢

# bz2.compress()和bz2.decompress()函数，
# 但是使用它们处理大文件的时候，必须分块读取文件内容，
# 否则会导致内存溢出。
# 这里我们演示如何使用BZ2File来操作大文件。

import bz2

with bz
