import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.resize(0)
    print(m.size())
    print(os.path.getsize('test'))
    m.flush()
    print(os.path.getsize('test'))
</code>
Output:
<code>1
1
0
</code>
I'm using Python 3.4.0. I tried it on Windows 7.

