import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # getting a ValueError: mmap slice assignment must be a single byte
    print(a)
</code>
The critical line is <code>a = m[:]</code>.


A:

I found that there's a difference between <code>mmap.mmap()</code> and <code>mmap.mmap().read()</code>
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m.read()
    print(a)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The first <code>print(a)</code> works, the second <code>print(a)</code> raises an exception

