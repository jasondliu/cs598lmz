import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
I'm using Python 3.6.3 on Windows 10.


A:

You need to call <code>mmap.flush()</code> after writing to the memory-mapped file.

