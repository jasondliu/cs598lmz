import bz2
bz2.decompress(d)

# 压缩与解压一个文件
# 压缩文件
with open('D:\pyworks\data.txt','rb') as f_in, bz2.BZ2File('D:\pyworks\data.bz2', 'wb') as f_out:
    f_out.writelines(f_in)

#解压文件
with bz2.BZ2File('D:\pyworks\data.bz2', 'rb') as f_in, open('D:\pyworks\data.txt', 'wb') as f_out:
    f_out.writelines(f_in)

# 读取bzip2压缩的文件
with bz2.open('D:\pyworks\data.bz2','rb') as f:
    f.read()


# LZMA压缩与解压
import lzma
with lzma.
