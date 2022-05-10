import mmap
# Test mmap.mmap(0, 0, '-')

import mmap

a = mmap.mmap(0, 0, '-')
b = mmap.mmap(-1, 0, '-')
print(a, b)
print(a.name, b.name)
print(a.length(), b.length())
print(a.tell(), b.tell())
print(a.readline(), b.readline())
print(a.read(), b.read())
print(a.readline(), b.readline())
print(a.read(), b.read())
print(a.seek(0), b.seek(0))
print(a.readline(), b.readline())
print(a.read(), b.read())
print(a.readline(), b.readline())
print(a.read(), b.read())
print(a.seek(0), b.seek(0))
print(a.readline(), b.readline())
print(a.read(), b.read())
