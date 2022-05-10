import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
</code>
This gives me a <code>TypeError: must be read-write buffer, not bytes</code>.
I know I can do this:
<code>m[0:1] = bytes(0)
m.flush()
</code>
But I want to know if there is a way to do it in one line.


A:

You can use <code>mmap.resize()</code> to truncate the file.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
</code>

