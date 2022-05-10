import bz2
bz2.decompress(bz2_data)

# 压缩和解压缩的数据必须是bytes类型的
# 如果是str类型的，需要先转换成bytes，然后再压缩和解压缩
# 压缩
bz2_data = bz2.compress(b'hello world')
# 解压缩
bz2.decompress(bz2_data)

# 压缩和解压缩的数据必须是bytes类型的
# 如果是str类型的，需要先转换成bytes，然后再压缩和解
