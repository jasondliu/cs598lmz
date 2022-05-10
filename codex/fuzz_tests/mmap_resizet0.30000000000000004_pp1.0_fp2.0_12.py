import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b'\x01'</code> on Windows, but <code>b''</code> on Linux.
I know that I can use <code>m.close()</code> before <code>f.truncate()</code> to get the same result on both platforms, but I'm curious why the behavior is different.

