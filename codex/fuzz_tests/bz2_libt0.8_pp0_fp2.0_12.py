import bz2
bz2_file = bz2.BZ2File('data/data.bz2')
for line in bz2_file:
    print(line)
bz2_file.close()

# gzip 压缩
import gzip
gzip_file = gzip.GzipFile('data/data.gz')
for line in gzip_file:
    print(line)
gzip_file.close()

# 压缩和解压缩 Base64
import base64
s = base64.b64encode(b'binary\x00string')
print(s)
d = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(d)

s = base64.b64encode('哈哈'.encode('utf-8'))
print(s)
d = base64.b64decode(b'5L2g5aW9')
print(d)

# 由于标准
