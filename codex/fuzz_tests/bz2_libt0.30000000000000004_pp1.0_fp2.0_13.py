import bz2
bz2.decompress(bz2_data)

# 压缩
bz2_comp = bz2.compress(data)

# 压缩文件
bz2.BZ2File('file.bz2', 'wb')

# 解压文件
bz2.BZ2File('file.bz2', 'rb')
