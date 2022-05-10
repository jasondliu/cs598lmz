from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
# 说明：为了提高性能，压缩文件格式一般都设计成块压缩的，
# 因此一个文件被分割成一个或多个块。
# 在压缩文件中，每个块都有自己的压缩编码，
# 并且在文件当中记录着这个块之前的同一段数据的位移。
# 对数据进行块压缩时，你可以使用 bz2 模块中
