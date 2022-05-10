import bz2
bz2.
 
bz2.BZ2File
bz2.BZ2Compressor
bz2.BZ2Decompressor


# 2.3 压缩文件
# 如果压缩文件大小，则更快
# 压缩文件也是一种 I/O 操作
# 更好的方式是使用上下文语法，以确保文件得到关闭

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with gzip.open('somefile2.gz', 'wt') as f:
    f.write(text)


# 注意：由于压缩数据不是文本，所以在读写时，必
