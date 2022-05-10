import bz2
bz2.decompress(data)

# 这个模块还包含一个open()函数，它接受一个filename参数，以及一些可选的参数以控制解压的操作。
# 与标准open()函数一样，这个函数返回一个文件对象，和标准文件对象一样，它支持读取和迭代。

with bz2.open('file.bz2', 'rt') as f:
    for line in f:
        print(line)

# 当写入的时候，你需要指定压缩级别
