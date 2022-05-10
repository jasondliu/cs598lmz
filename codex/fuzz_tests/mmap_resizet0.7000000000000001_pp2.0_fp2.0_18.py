import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(len(a))
    m.close()
</code>
If you need to change the size of the file, you need to use <code>mmap.resize()</code> instead of <code>truncate()</code>.

