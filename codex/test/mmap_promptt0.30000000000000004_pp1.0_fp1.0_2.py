import mmap
# Test mmap.mmap.readline()

with open('/proc/cpuinfo', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
        print(m.readline())
