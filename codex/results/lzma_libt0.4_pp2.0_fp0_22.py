import lzma
lzma.open("/Users/xue/Downloads/moby_dick.txt.xz")

# 压缩和解压缩的数据必须是二进制数据
# 如果是文本数据，需要先使用encode()方法编码为二进制数据

data = b"Lots of data here"
with gzip.open("/tmp/example.txt.gz", "wb") as f:
    f.write(data)

with gzip.open("/tmp/example.txt.gz", "rb") as f:
    print(f.read())

# 压缩文件
import gzip
import shutil
with open("/tmp/example.txt", "rb") as f_in:
    with gzip.open("/tmp/example.txt.gz", "wb") as f
