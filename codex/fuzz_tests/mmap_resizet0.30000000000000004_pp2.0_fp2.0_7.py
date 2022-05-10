import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The result is <code>b'\x01'</code>, but I expected <code>b''</code> (empty byte string).
I also tried to use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> and <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)</code> instead of <code>mmap.mmap(f.fileno(), 0)</code>, but the result is the same.
What's wrong?


A:

The problem is that the <code>mmap</code> object is still referring to the original file size, which is 1 byte.
You can use <code>m.resize(0)</code> to resize the <code>mmap</code> object to match the new file size.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.res
