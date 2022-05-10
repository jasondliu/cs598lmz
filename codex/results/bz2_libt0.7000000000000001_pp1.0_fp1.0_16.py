import bz2
bz2.open('__init__.py', 'rb')

# 压缩文件写入
import bz2
import io
f = io.BytesIO()
with bz2.open(f, 'wb') as output:
    output.write(b'binary data')
f.seek(0)
f.read()

import bz2
with bz2.open('data.bz2', 'wt') as output:
    output.write('Hello World!')

import bz2
with bz2.open('data.bz2', 'rt') as input:
    print(input.read())


# 压缩和解压缩
import bz2
compressed = bz2.compress(b'binary data')
print(compressed)

print(bz2.decompress(compressed))

print(bz2.decompress(b'BZh91AY&SY\x94\x8e\x0c \x00\x00\x00
