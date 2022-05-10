import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())

# print(help(m))

# https://python-forum.io/Thread-Why-is-mmap-read-seemingly-randomly-failing?pid=126585#pid126585

# m.seek(0)
# print(m.read())
# m.seek(0)
# print(m.read())
