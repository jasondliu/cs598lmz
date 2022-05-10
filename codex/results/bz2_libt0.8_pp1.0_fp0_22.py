import bz2
bz2.BZ2Decompressor().decompress(bz2.BZ2File('xaa.tar.bz2', 'r').read())

# 如果只需要读取一小部分，上面的代码会把全部数据读入内存
bz2.BZ2Decompressor().decompress(bz2.BZ2File('xaa.tar.bz2', 'r').read(100))

# 要在不同的数据块中使用多个压缩和解压对象
dec = bz2.BZ2Decompressor()
data = dec.decompress(bz2.BZ2File('xaa.tar.bz2', 'r').read(100))
data += dec.decompress(bz2.BZ2File('xaa.tar.b
