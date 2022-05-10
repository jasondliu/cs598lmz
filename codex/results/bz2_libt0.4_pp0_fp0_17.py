import bz2
bz2.decompress(bz2_data)

# 压缩
bz2_compressed = bz2.compress(data)
bz2_compressed

# 压缩文件
bz2_file = bz2.BZ2File('bz2_file.bz2', 'w')
bz2_file.write(data)
bz2_file.close()

# 解压文件
bz2_file = bz2.BZ2File('bz2_file.bz2', 'r')
bz2_file.read()
bz2_file.close()

# 压缩文件
with bz2.BZ2File('bz2_file.bz2', 'w') as bz2_file:
    bz2_file.write(data)

# 解压文件
with bz2.BZ2File('bz2_file.bz2', 'r') as
