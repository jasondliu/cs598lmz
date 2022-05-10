import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
When I run the code, I get a <code>ValueError: mmap offset is greater than file size</code>.
I tried to read the documentation, but I didn't find any solution.
I'm using Python 3.6.2 on Windows 10.


A:

You are using <code>mmap</code> incorrectly. The first argument to <code>mmap</code> is the length of the mapped region, not the file descriptor.
<code>m = mmap.mmap(0, f.fileno(), 0)
</code>
You should use <code>mmap.ALLOCATIONGRANULARITY</code> as the length if you want to map the whole file.
<code>m = mmap.mmap(0, mmap.ALLOCATIONGRANULARITY, 0)
</code>

