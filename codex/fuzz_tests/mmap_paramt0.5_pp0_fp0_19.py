import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = bytes(2)
    print(m[0])
</code>
This prints <code>1</code> and <code>2</code> on my system.

