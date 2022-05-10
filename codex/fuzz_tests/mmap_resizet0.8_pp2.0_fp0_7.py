import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
its prints: <code>b'\x00'</code>
Is it a bug? Did I miss something? How to fix it?


A:

Looks like the file handle is kept in the class instance. That's the reason why you got the correct <code>b'\x01'</code> even if truncate was called.
You can use <code>m.close()</code> to check it out.
<code>from mmap import mmap, ACCESS_READ

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
    m = mmap(f.fileno(), 0, access=ACCESS_READ)
    a = m[:]
    print(a)
</code>
See the mmap docs for more details.

