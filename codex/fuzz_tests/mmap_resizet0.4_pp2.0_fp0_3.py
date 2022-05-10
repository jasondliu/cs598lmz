import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I've tried <code>m.flush()</code> and <code>m.close()</code> before the <code>truncate</code> call, but it didn't help.
I'm using Python 3.5.1 on Windows.


A:

This is a bug in Python 3.5.1 on Windows. It's fixed in 3.5.2.

