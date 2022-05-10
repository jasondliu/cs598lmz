from bz2 import BZ2Decompressor
BZ2Decompressor(bz2_data)

# 压缩数据
data = b'ABC' * 10
comp = BZ2Compressor()
comp.compress(data)
comp.flush()

# 压缩文件
import os
with open('/tmp/example.txt', 'wt') as f:
    f.write('content')

with open('/tmp/example.txt', 'rb') as input:
    with bz2.BZ2File('/tmp/example.txt.bz2', 'wb') as output:
        output.writelines(input)
os.system('file /tmp/example.txt.bz2')

# 解压缩文件
import bz2
with bz2.BZ2File('/tmp/example.txt.bz2', 'rb') as input:
    with open('/tmp/example.txt', 'wb') as output:
        for line in input:
            output.write(line)
os.system('file /tmp/example.
