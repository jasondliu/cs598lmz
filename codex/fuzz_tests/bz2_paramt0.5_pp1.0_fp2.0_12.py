from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

# 把上面一段代码变成一个函数
def bz2_decompress(data):
    return BZ2Decompressor().decompress(data)

# 另外一种写法，使用lambda函数
bz2_decompress = lambda data: BZ2Decompressor().decompress(data)

# 使用functools.partial可以做到同样的效果
from functools import partial
bz2_decompress = partial(BZ2Decompressor().decompress)

