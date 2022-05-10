import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected <code>a</code> to be <code>b''</code>, but it's <code>b'\x01'</code>.
Why is that?


A:

The <code>mmap</code> object is not updated when the file is truncated. You need to call <code>mmap.resize()</code> to resize the mapping:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
</code>
The <code>mmap</code> object is now empty.

