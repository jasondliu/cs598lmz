import lzma
lzma.LZMAFile

# lzma.LZMAFile(filename=None, mode="r", fileobj=None, format=None, check=-1, preset=None, filters=None)

# 创建一个LZMAFile对象，可以像普通文件一样读写
# filename: 压缩文件的路径
# mode: 压缩文件的打开模式，可选值为"r", "rb", "w", "wb", "x", "xb", "a", "ab"
# fileobj: 一个可读写的二进制文件对象
# format: 压缩文件的格式，可选值为"xz"或"alone"
# check: 校验类
