import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this example, the mmap is still referring to the old file size. How can I make it refer to the new file size?


A:

<code>mmap.mmap</code> objects are not resizable, so you need to create a new one.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>

