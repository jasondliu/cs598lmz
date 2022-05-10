import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# 将一个文件压缩后再解压缩
with open('test.txt', 'rb') as f_in, bz2.open('test.bz2', 'wb') as f_out:
    f_out.writelines(f_in)

with bz2.open('test.bz2', 'rb') as f_in, open('test.txt', 'wb') as f_out:
    f_out.writelines(f_in)

# 压缩和解压缩文件时，可以指定一个压缩级别，从1到9，级别越高，压缩的越好，但是速度越慢
with open('test.
