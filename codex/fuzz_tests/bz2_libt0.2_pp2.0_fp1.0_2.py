import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# bz2.compress() 和 bz2.decompress() 函数分别对数据进行压缩和解压缩。
# 另外，还有一个 BZ2File 类，它用于操作 bzip2 格式的压缩文件。

# 压缩文件
with bz2.BZ2File('spam.bz2', 'w') as f:
    f.write(b'Hello World!')

# 解压文件
with bz2.BZ2File('spam.bz2', 'r') as f:
    print(f.read())

# 压缩文件的压缩率比 gzip 模
