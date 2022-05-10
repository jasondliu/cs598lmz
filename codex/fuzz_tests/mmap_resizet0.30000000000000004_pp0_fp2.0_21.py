import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect <code>a</code> to be <code>b'\x01'</code>, but it is <code>b''</code>.
I know that I can use <code>mmap.resize</code> to change the size of the mmap, but I want to know why the above code doesn't work.

