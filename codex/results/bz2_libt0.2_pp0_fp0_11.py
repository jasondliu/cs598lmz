import bz2
bz2.decompress(bz2.compress(b'Hello World'))

# 压缩和解压文件
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.write('Hello World')
with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# 压缩和解压文件
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.write('Hello World')
with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# 压缩和解压文件
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.write('Hello World')
with bz2.open('file.bz2', 'rt') as f
