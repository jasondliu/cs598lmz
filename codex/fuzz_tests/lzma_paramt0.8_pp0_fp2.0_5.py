from lzma import LZMADecompressor
LZMADecompressor

# lzma模块允许对一个文件进行压缩，或从一个压缩的文件中读取数据。
#
# 压缩的结果实际上是一个标准文件对象，它同时实现了普通文件对象的接口，从而可以替代标准文件对象。
#
# lzma.open() 方法接受一个文件名作为参数，并根据提供的模式，打开一个文件，并将其返回为
