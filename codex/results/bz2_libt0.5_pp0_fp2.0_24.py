import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# 小文件压缩
import bz2
f = open('file.txt', 'rb')
data = f.read()
f.close()
compressed = bz2.compress(data)
f = open('file.bz2', 'wb')
f.write(compressed)
f.close()

# 大文件压缩
import bz2
f = bz2.BZ2File('file.bz2', 'wb')
f.write(b'Hello World!')
f.close()

# 大文件解压缩
import bz2
f = bz2.BZ2File('file.bz2', 'rb')
data = f.read()
f.close()

# 压缩等级
import bz2
f = bz2.BZ2File('file.bz2', 'wb', compresslevel
