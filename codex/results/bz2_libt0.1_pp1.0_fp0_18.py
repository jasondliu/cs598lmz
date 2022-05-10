import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.write('hello world')

# 解压文件
import bz2
with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# 压缩文件
import bz2
with open('file.txt', 'rt') as f_in, bz2.open('file.bz2', 'wt') as f_out:
    f_out.writelines(f_in)

# 解压文件
import bz2
with bz2.open('file.bz2', 'rt') as f_in, open('file.txt', 'wt') as f_out:
    f_out.writelines(f_in)

# 压缩文件
import
