import bz2
bz2.decompress(bz2_data)

# 对于文本文件，可以用BZ2File代替open()来操作
with bz2.BZ2File('sample.bz2') as f:
    data = f.read()

# 压缩
with open('sample.txt', 'rb') as f_in, bz2.BZ2File('sample.bz2', 'wb') as f_out:
    f_out.writelines(f_in)

# 压缩级别
# 默认是9，可以指定压缩级别0-9
with bz2.BZ2File('sample.bz2', 'wb', compresslevel=5) as f:
    f.write(b'123')

# 压缩
data = bz2.compress(b'123')
# 解压
