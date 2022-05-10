import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    m[0] = 2
</code>
The <code>mmap</code> documentation says that it just calls <code>open</code> with the <code>O_RDWR</code> flag. I'm not sure if there's any difference between opening a file with <code>O_RDWR</code> and <code>O_RDONLY</code> and then calling <code>open</code> with <code>O_WRONLY</code>.

