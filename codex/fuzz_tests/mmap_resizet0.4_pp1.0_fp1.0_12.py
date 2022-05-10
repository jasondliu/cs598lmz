import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I thought the result would be <code>b'\x01'</code>, but the result is <code>b''</code>.
I want to know why and how to get <code>b'\x01'</code>?


A:

The problem is that the <code>mmap</code> is tied to the file descriptor.  So when you truncate the file, the <code>mmap</code> is still tied to the file descriptor, which is now empty.
The solution is to use <code>mmap.MAP_SHARED</code> when you create the <code>mmap</code> object.  This will cause the <code>mmap</code> object to be updated when the file is changed.
<code>m = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED)
</code>

