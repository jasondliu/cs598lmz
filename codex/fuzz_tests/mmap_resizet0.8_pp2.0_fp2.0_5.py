import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
What causes this behavior?
Is there a way to make this work without looping manually over the file and writing it out?


A:

The <code>mmap</code> object is now pointing to invalid memory.  You need to call <code>m.close()</code> before you truncate the file or the file must be opened without <code>write</code> permissions on the <code>f</code> file object.

