import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))

with open('test') as f:
    print(f.read())

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    print(m.read(1))
</code>
This prints out:
<code>b'\x02'
2
2
</code>
Does anyone know what's going on here?


A:

The reason is that the <code>mmap</code> object is a window over a fixed range of bytes in the file.  It has no knowledge of the difference between bytes that are part of the file and bytes that are part of the window.  When you <code>write</code> to the <code>mmap</code>, it writes to the window, and when you <code>read</code> from the <code>mmap</code>, it reads from the window.  But the window is fixed, so <code>
