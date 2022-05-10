import bz2
bz2.decompress(bz2.compress(bytes(range(256))))

# bz2.compress() 函数将字符串压缩成一个字节序列，而 bz2.decompress() 函数将它们解压缩。
# 与 zlib.compress() 函数类似，bz2.compress() 函数还接受一个可选的参数用于控制压缩级别。
# 该参数的值介于 1 到 9 之间，数字越大，压缩级别越高，但是压缩时间也越长。

# 另一个
