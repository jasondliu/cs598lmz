import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The result is <code>b'\x00'</code> instead of <code>b'\x01'</code>.
Why is that?
I know I can use <code>mmap.resize</code>, but I don't know the size of the file in advance.

