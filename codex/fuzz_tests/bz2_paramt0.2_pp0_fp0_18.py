from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# 如果你想使用压缩文件的方式来处理数据，可以使用 open() 函数的 compresslevel 参数。
# 下面是一个将数据压缩到一个文件中的例子：
with open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(data)

# 压缩级别是一个从 1 到 9 的整数，表示压缩算法的压缩比。
# 数字越大，压缩比越大，但是耗费的 CPU 时间
