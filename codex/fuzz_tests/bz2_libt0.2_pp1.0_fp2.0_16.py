import bz2
bz2.BZ2File(filename, 'w')

# 写入压缩数据
with bz2.BZ2File('spam.bz2', 'w') as f:
    f.write(b'Hello World')

# 读取压缩数据
with bz2.BZ2File('spam.bz2', 'r') as f:
    print(f.read())

# 压缩文件
import bz2
uncompressed_data = b'Hello World'
with bz2.BZ2File('spam.bz2', 'wb') as f:
    f.write(uncompressed_data)

# 解压文件
import bz2
with bz2.BZ2File('spam.bz2', 'rb') as f:
    print(f.read())

# 压缩文件
import bz2
uncompressed_data = b'Hello
