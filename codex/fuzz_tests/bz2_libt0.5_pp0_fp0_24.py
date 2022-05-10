import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# 使用bz2压缩文件
with open('file.txt', 'rb') as f, bz2.open('file.txt.bz2', 'wb') as bz2_file:
    bz2_file.writelines(f)

with bz2.open('file.txt.bz2', 'rb') as bz2_file, open('file.txt', 'wb') as f:
    f.writelines(bz2_file)
