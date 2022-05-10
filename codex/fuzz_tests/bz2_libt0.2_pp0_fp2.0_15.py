import bz2
bz2.decompress(bz2.compress(data))

# bz2.compress() 和 bz2.decompress() 函数分别压缩和解压缩一个字符串。
# 如果你像操作文件一样操作压缩数据，你可以使用 BZ2File 类。例如：

with bz2.BZ2File('spam.bz2', 'wb') as f:
    f.write(data)

with bz2.BZ2File('spam.bz2', 'rb') as f:
    print(f.read())

# 如果你想在内存中压缩数据，你可以使用 BytesIO() 对象
