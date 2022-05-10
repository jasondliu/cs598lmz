import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an <code>IndexError</code> for line 8. How can I create a process-shared memory map that does not back on any file or region?


A:

The <code>mmap</code> builtin function constructs a new object.  You need to use the <code>mmap()</code> method on an <code>mmap</code> object to expand it.  This can be done without a file descriptor.
<code>import mmap

m = mmap.mmap(-1, 1)
m.mmap(0, 2, m.ACCESS_WRITE)
</code>
(Documentation link.)

