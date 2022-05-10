import lzma
lzma.compress(b'Hello World', preset=0)

# 压缩文件
with open('test.txt', 'rb') as f:
    data = f.read()
with lzma.open('test.xz', 'wb') as f:
    f.write(data)

# 解压文件
with lzma.open('test.xz', 'rb') as f:
    data = f.read()
with open('test.txt', 'wb') as f:
    f.write(data)


# 内存映射
import mmap
with open('test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())
    print(m.readline())
    print(m.readline())
    print(repr(m.readline()))
    m.seek(0)
    out = m.read()
    print(out)
    m.seek(0)

