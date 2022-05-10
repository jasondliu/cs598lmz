import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises a <code>ValueError</code> with the message <code>mmap: can't resize a read-only or copy-on-write memory map</code>.
I've tried to work around this by using <code>mmap.ACCESS_WRITE</code> instead of <code>mmap.ACCESS_COPY</code>, but then I get a <code>ValueError</code> with the message <code>mmap: invalid access parameter</code>.
I've also tried to use <code>mmap.resize()</code> instead of <code>f.truncate()</code>, but that raises a <code>ValueError</code> with the message <code>mmap: can't resize a read-only or copy-on-write memory map</code>.
I've also tried to use <code>mmap.resize()</code> before reading from the memory map, but that also raises a <code>ValueError</code> with the message <code>mmap: can't resize a read-only or copy-on-write memory map</code>.
I've also tried to
