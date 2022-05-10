import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())

# mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT)
# fileno: 文件描述符
# length: 可选，指定映射的长度，如果为0，则表示从当前文件位置到文件末尾。
# flags: 可选，MAP_SHARED（共享）和MAP_PRIVATE（私有）。
# prot: 可选，PROT_READ（读）、PROT_WRITE（写）和PROT_EXEC
