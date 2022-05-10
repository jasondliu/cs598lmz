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
with open('file.txt', 'rt') as f:
    data = f.read()
with bz2.open('file.bz2', 'wt') as f:
    f.write(data)

# 解压文件
import bz2
with bz2.open('file.bz2', 'rt') as f:
    data = f.read()
with open('file.txt', 'wt') as f:
    f.write(data)

# 压缩文件
