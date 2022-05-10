import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>.
I was expecting <code>b''</code>.
Why is that?


A:

The <code>mmap</code> object is still pointing to the same location in the file, even though the file has been truncated. The memory is still there, but the file no longer contains any data.

