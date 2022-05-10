import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This gives me an <code>IndexError: mmap index out of range</code>.
Any ideas?


A:

You cannot resize a mmapped file.
You can create a new mmap of the new size, then copy the old data to the new mmap.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    data = m[:]
    m.close()
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    m[:] = data
    m.close()
</code>

