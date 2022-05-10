import bz2
bz2.decompress(bz2.compress(b"Hello, World!"))

# 在使用 bz2 模块时，要注意的是它不支持随机访问，因此只能对整个文件进行压缩或解压缩。
# 如果文件很大，或者是个生成器，那么这个限制就可能成为问题。

# 可以使用 BZ2File 类来创建一个文件对象，然后像处理普通文件一样来处理它。

import bz2
with bz2
