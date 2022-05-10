import mmap
# Test mmap.mmap for small files

with open('small.txt', 'wb') as f:
    f.write(b'i'*(1024*1024*10))

print('this is a small file', file=open('small.txt', 'a'))

with open('small.txt', 'rb') as f:
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(len(s))
    print(type(s))
    print(s.readline().decode())
    print(s.tell())
    print(s.tell()%512)
    print(s.tell()//512)
    print(s.readline().decode())
    print(s.readline().decode())
    print(s.readline().decode())
    print(s.readline().decode())
    print(s.readline().decode())
    print(s.readline().decode())
    print(s.readline().decode())
    print(s.readline().decode())

