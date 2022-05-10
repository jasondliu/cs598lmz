import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2 模块还支持一个压缩级别的参数，它是一个介于 1 和 9 之间的整数，表示压缩算法的速度与压缩比之间的平衡。
# 数字越大，压缩越慢，但压缩比也越高。默认值为 9。

# 如果要同时读写一个 bz2 文件，那么你必须使用 BZ2File 对象，它同时支
