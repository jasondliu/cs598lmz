from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 注意：

# 如果对象文件关闭，那么无法操作压缩数据。 因此，在使用时，应该永久保存压缩文件的引用。
# bz2 模块在每一次压缩与解压时都需要创建一个新的解压器或者是压缩器。 创建压缩或者解压器的开销大，
# 所以最好的方式是创建一个解压器或
