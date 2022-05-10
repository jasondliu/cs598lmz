import bz2
bz2.decompress(bz2.compress(str.encode('hello world')))

# 参数是一个可选的标志，指定压缩算法，默认值是9，表示最高压缩率，而1则表示最低压缩率，0表示没有压缩。
# 压缩率等级越高，压缩后文件的大小越小，但是压缩速度也越慢，解压速度也越慢。

# bz2模块还提供了一个BZ2
