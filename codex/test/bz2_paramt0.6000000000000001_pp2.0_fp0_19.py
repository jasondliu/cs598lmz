from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')

# 创建一个BZ2Compressor对象，然后向它传入数据并不断地调用compress()方法，最后调用flush()方法来生成压缩文件的最后部分。
from bz2 import BZ2Compressor
compressor = BZ2Compressor()
compressor.compress(b'hello world!')
compressor.flush()

# 使用lzma压缩
# lzma模块可以压缩和解压缩.xz文件
import lzma
