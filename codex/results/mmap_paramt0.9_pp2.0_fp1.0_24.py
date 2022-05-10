import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes([4])
    
with open('test') as f:
    print(f.read())

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes([4])
    m.flush()
    print(f.read())
</code>
When you open a file in Windows in <code>r+b</code> mode, it's shared mode is <code>FILE_SHARE_WRITE</code>. To read a mmap you first must open in read mode so the share mode is <code>FILE_SHARE_READ</code>.
Reference: https://docs.python.org/3/library/mmap.html#mmap.mmap

