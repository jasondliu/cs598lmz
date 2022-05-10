from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(data))

# 其他压缩方式
# 压缩数据的最终目标是压缩文件，而不是压缩单个字符串。
# zlib模块提供了一个类来处理单个文件，而不是像压缩和解压缩函数那样处理字节对象。
# 为了创建一个压缩文件，你需要创建一个压缩对象，然后将数据写入到它上面。
import z
