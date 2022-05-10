import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0,
                  access=mmap.ACCESS_READ | mmap.ACCESS_WRITE)
    with open('data', 'r+b') as f2:
        m2 = mmap.mmap(f2.fileno(), 0,
                       access=mmap.ACCESS_READ | mmap.ACCESS_WRITE)

print(m[0])
print(m2[1])
</code>
This somehow works, but I need to know if there is a better solution than allocating huge memory maps.

