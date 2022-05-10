import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get an <code>IndexError: memory access out of range</code> error in the last line. Why is that?


A:

The <code>mmap</code> is still pointing to the old map, so if you truncate or change the size, it will still be pointing at the old size. You can use <code>mmap.resize</code> to change the size of the mapped area.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(f.tell())
    a = m[:]
</code>

