from lzma import LZMADecompressor
LZMADecompressor().decompress(xz_data)

# 解压缩bz2压缩文件
import bz2
bz2_data = bz2.decompress(bz2_data)

# 解压缩gzip压缩文件
import gzip
gzip_data = gzip.decompress(gzip_data)
