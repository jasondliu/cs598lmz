import bz2
bz2.decompress(bz2_data)

# bz2_data = bz2.compress(data)
# bz2.decompress(bz2_data)

# 另一种方法是使用BZ2File类，它会返回一个类似于普通文件对象的东西，
# 可以用在with语句中，并且支持像read()和write()方法一样的操作
# with bz2.BZ2File('file.bz2') as f:
#     data = f.read()

# 如果要压缩的数据很小，建议使用zlib，因为它的压缩速度
