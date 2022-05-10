import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[0] = ord('3')
    print(m[0])

# 如果缓冲区被改变，就需要调用flush()来将缓冲区的被写入文件
import os

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    print(m.size())
    m.write(b'a')
    m.seek(0)
    print(m.read(1))
    m.flush()
