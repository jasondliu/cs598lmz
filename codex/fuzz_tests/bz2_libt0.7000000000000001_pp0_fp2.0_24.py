import bz2
bz2.decompress(bz2.compress(b"hello world"))

# 此外，还有一些通用的输入输出函数，比如memoryview和fileIO。
# memoryview: 内存的切片对象
# fileIO: 文件的读写操作
