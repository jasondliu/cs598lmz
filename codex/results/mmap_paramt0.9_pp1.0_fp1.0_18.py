import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[0] = b'a'

with open('test', 'r') as f:
    print(f.readlines())
</code>
But the file is not changed. Why? How do I change the file using mmap?

