import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
When I run it, I got <code>ValueError: mmap closed or invalid</code>.
But if I comment out the <code>m.close()</code> line, it prints out <code>b'\x01'</code>.
So my question is, how can I close the mmap after truncating the file?


A:

After the file is truncated, the mmap is invalidated. 
In your example, after <code>f.truncate()</code>, the file is empty and the mmap points to a non-existing area.
The simplest solution is to recreate the mmap after the file is truncated.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    print(a)
    m.close()
</code>

