import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = b'a'
    m.close()
</code>
I know that it can be done with <code>fcntl</code> but I don't want to use it because of its portability.

