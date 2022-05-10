from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#接受可选的max_length参数，设置被解压的最大字节数
d = BZ2Decompressor()
d.decompress(data, max_length=100)

#如果还有更多的数据，就调用BZ2Decompressor.decompress()，否则调用BZ2Decompressor.flush()
d = BZ2Decompressor()
d.decompress(data1)
d.decompress(data2)
d.flush()


#zlib模块
import zlib
s = b'witch which has which witches wrist watch'
len(s)

#32
t = zlib.compress(s)
#42
len(t)

zlib.decompress(t)

zlib.crc32(
