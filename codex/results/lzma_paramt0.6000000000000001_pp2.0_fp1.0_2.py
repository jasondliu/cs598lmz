from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# 使用更高级的压缩格式，比如bzip2，需要一个第三方包，比如bz2：
import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed)

# 压缩数据的通用做法是先创建一个压缩对象，然后不断的调用它的压缩方法，最后调用flush()方法来生成最终的压缩数据。
# 解压
