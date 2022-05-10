import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 另一个压缩方法就是使用 bz2 模块，它提供的压缩和解压缩的算法和 lzma 类似，
# 但是速度更快，数据压缩率也不那么高。
import bz2
bz2.compress(b'hello world')

# 如果你想控制压缩级别，可以在压缩对象上使用 compress() 方法，
# 它接受一个介于 1 和 9 之间的整数作为
