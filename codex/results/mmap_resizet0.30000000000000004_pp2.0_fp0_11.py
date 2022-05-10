import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives me a <code>ValueError: mmap offset is greater than file size</code> on the last line.
I'm using Python 3.6.1 on Linux.
I've tried <code>m.resize(0)</code> before the <code>truncate</code> call, but that gives me <code>ValueError: mmap can't resize a read-only or copy-on-write (COW) mapping</code>.
I've tried <code>m.resize(0)</code> after the <code>truncate</code> call, but that gives me <code>ValueError: mmap can't resize a read-only or copy-on-write (COW) mapping</code>.
I've tried <code>m.resize(0)</code> after the <code>truncate</code> call and then <code>m.close()</code> and then <code>m = mmap.mmap(f.fileno(), 0)</code>, but that gives me <code>ValueError: mmap offset is greater than file size</code>.
I've tried <
