from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 如果你想处理的数据是一个文件，而不是字符串，你可以使用一个 BZ2File 对象来代替。
# 比如，下面这个例子展示了如何将一个大文件压缩后再解压缩：

import bz2
uncompressed = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
with bz2.BZ2File('un
