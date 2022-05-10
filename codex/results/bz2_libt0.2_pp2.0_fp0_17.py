import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
import bz2
f = bz2.BZ2File('file.bz2', 'wb')
f.write(b'hello world')
f.close()

# 解压文件
import bz2
f = bz2.BZ2File('file.bz2', 'rb')
print(f.read())
f.close()

# 压缩文件
import bz2
f = bz2.open('file.bz2', 'wt')
f.write('hello world')
f.close()

# 解压文件
import bz2
f = bz2.open('file.bz2', 'rt')
print(f.read())
f.close()

# 压缩文件
import bz2
with bz2.open('file.bz2', 'wt') as f:
   
