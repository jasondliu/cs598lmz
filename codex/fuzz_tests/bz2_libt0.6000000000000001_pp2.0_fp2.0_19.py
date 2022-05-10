import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# 可以看出bz2的压缩比比zlib要好，但是速度慢
import time
source = b'Welcome to Beijing!'
for i in range(5):
    start = time.time()
    zlib.compress(source)
    end = time.time()
    print('Zlib compress:', end - start)
for i in range(5):
    start = time.time()
    bz2.compress(source)
    end = time.time()
    print('Bz2 compress:', end - start)

# 压缩文件
# zlib.compress()和zlib.decompress()只能处理bytes类型的数据，如果要处理文本，需要先将文
