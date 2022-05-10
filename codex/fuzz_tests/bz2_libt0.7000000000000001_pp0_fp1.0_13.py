import bz2
bz2.BZ2Compressor().compress(b"hello world!")

# 如果一个文件用bz2压缩过，那么在Python中就可以直接读取它。
# 同样也支持通过压缩文件对象来写入压缩文件。

import bz2
with bz2.open('filepath', 'rb') as input:
    print(input.read(100))

with bz2.open('filepath', 'wb') as output:
    output.write(b"hello world!")

# 在使用bz2压缩文件的时候，也可以制定一个压缩级别。
# 这个值是一个1
