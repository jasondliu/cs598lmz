import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.flush()
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
</code>
The output is <code>b'\x01'</code> instead of <code>b'\x00'</code>.


A:

The <code>flush()</code> method is meant to be used when you are using the <code>mmap</code> object as a file-like object, not when you are using it as a memory-mapped object.
If you want to unmap the memory-mapped object, use the <code>close()</code> method.

