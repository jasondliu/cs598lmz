import bz2
bz2.compress(b'hello world')

# 解压
bz2.decompress(b'BZh91AY&SY\x94\x8e\x0e\x00\x00\x00\x81\x04\x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# 使用bz2.compress()和bz2.decompress()单独处理压缩和解压数据，
# 如果数据量比较大，可以使用BZ2File类来处理文件，
# BZ2File类会在压缩和解压时自动处理缓冲，
# 并且可
