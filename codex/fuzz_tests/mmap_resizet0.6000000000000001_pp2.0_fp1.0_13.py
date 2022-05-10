import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
<code>a</code> is empty.
Why is <code>mmap</code> not updated after <code>truncate</code>?


A:

The issue is that the underlying mmap object was created when the file was size 1. The <code>mmap</code> object itself is just a wrapper around the underlying file, it doesn't really do anything on its own. 
The file was truncated to 0, but mmap doesn't know about that. It's still pointing to the original file.
You can get around this by using mmap's <code>resize()</code> method.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
    print(a)
</code>

