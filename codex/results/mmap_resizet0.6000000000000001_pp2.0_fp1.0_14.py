import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This results in a <code>ValueError</code> exception:
<code>ValueError: mmap offset is greater than file size
</code>
I've tried to use <code>mmap.resize</code> and <code>mmap.resizeable</code> to fix the issue, but I'm still getting the same error.
I'm using Python 3.6.1 on Linux (Ubuntu 16.04)


A:

When you do <code>f.truncate()</code> it will change the file size to 0 byte. As you don't specify the size, it will be 0 byte.
<code>mmap.mmap</code> will create a file view starting at the specified offset. If the offset is greater than the file size, it will raise a <code>ValueError</code>.
You should specify the size when you do <code>f.truncate()</code>.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m =
