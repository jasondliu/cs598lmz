import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
import bz2
with open('/Users/michael/notexist.txt', 'rb') as f:
    data = f.read()
with bz2.open('/Users/michael/notexist.bz2', 'wb') as f:
    f.write(data)
with bz2.open('/Users/michael/notexist.bz2', 'rb') as f:
    data = f.read()
print(data)

# 压缩文件
import gzip
with open('/Users/michael/notexist.txt', 'rb') as f:
    data = f.read()
with gzip.open('/Users/michael/notexist.gz', 'wb') as f:
    f.write(data)
with gzip.open('/Users/michael/notexist.gz', 'rb') as f:
    data = f.read()
print(data)


