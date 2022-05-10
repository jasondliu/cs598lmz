from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 实际上，这个类的功能就是创建一个BZ2压缩对象，然后用它来解压数据。
# 下面是一个简单的例子，使用一个压缩文件对象来读取压缩数据。

import bz2
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x
