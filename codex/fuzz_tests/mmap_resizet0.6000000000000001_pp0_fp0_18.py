import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line fails with <code>mmap.error: [Errno 9] Bad file descriptor</code>.
I assume <code>f.truncate()</code> invalidates the mmap, but is there a way to preserve it?


A:

I'm not sure if this is what you're looking for, but you can use <code>m.resize(0)</code> to truncate the file.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
</code>
This seems to work for me.

