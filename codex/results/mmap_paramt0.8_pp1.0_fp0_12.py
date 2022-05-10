import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(0xfff)
    print(len(m))
    print(sys.getsizeof(m))
    m.close()
</code>

