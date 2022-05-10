from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# 在使用BZ2压缩数据的时候，你需要注意的是它并不能保存文件元数据（比如文件名或者其他的描述性信息）。
# 如果你想保存这些信息的话，可以使用tarfile或者zipfile模块来打包你的数据，然后再压缩。

# 如果你有一个大型的二进制数组，并希望在压缩的同时节省内存
