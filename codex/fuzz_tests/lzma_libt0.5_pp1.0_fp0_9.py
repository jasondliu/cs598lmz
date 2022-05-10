import lzma
lzma.decompress(open('../data/data.lzma', 'rb').read())

# 使用lzma模块进行压缩
lzma.compress(open('../data/data.txt', 'rb').read())

# 使用lzma模块进行解压缩
lzma.decompress(open('../data/data.lzma', 'rb').read())

# 使用gzip压缩文件
import gzip
gzip.compress(open('../data/data.txt', 'rb').read())

# 使用gzip解压缩文件
gzip.decompress(open('../data/data.lzma', 'rb').read())

# 使用bz2压缩文件
import bz2
bz2.compress(open('../data/data.txt', 'rb').read
