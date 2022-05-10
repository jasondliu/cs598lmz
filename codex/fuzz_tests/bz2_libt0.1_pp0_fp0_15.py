import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
with bz2.BZ2File('test.bz2', 'w') as f:
    f.write(b'hello world')

# 解压文件
with bz2.BZ2File('test.bz2', 'r') as f:
    print(f.read())

# 压缩文件
with open('test.txt', 'rb') as f_in, bz2.BZ2File('test.bz2', 'wb') as f_out:
    f_out.writelines(f_in)

# 解压文件
with bz2.BZ2File('test.bz2', 'rb') as f_in, open('test.txt', 'wb') as f_out:
    f_out.writelines(f_in)
