import bz2
bz2.decompress(data)

# 使用bz2模块的BZ2Compressor和BZ2Decompressor类可以创建压缩器和解压程序对象，
# 可以分块处理大文件

compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data)


# zlib模块提供了通用的数据打包和压缩功能，和gzip模块类似，zlib模块的压缩和解压程序
#
