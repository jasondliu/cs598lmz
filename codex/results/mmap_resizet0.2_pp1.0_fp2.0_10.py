import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It works fine on Linux, but on Windows it raises <code>ValueError: mmap offset is greater than file size</code>.
I've tried to use <code>mmap.ACCESS_READ</code> instead of <code>mmap.ACCESS_WRITE</code>, but it doesn't help.
Is there a way to make it work on Windows?


A:

I've found a solution:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
</code>

