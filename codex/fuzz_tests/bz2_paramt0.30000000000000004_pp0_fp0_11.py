from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# 压缩文件
# 压缩文件的操作是一个很好的例子，因为它演示了如何使用压缩对象来处理大量的数据。
# 在这个例子中，我们将一个文件读取到内存中，然后将它压缩后写入另一个文件。
# 压缩文件的代码如下：
import bz2
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00
