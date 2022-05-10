import bz2
bz2.decompress(bz2_data)

# 使用bz2模块压缩数据

import bz2
bz2_data = bz2.compress(b'this is a test')
print(bz2_data)

# 使用bz2模块对文件进行压缩

import bz2
uncompressed_data = b'This is a test.'
with bz2.BZ2File('uncompressed.txt', 'wb') as f:
    f.write(uncompressed_data)

with bz2.BZ2File('compressed.bz2', 'wb') as f:
    f.write(uncompressed_data)

# 使用bz2模块对文件进行解压缩

import bz2
with bz2.BZ2File('compressed.bz2', '
