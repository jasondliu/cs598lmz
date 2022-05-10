import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In the last line, the value of <code>a</code> is <code>b''</code>.
Why does this happen?


A:

You asked a similar question already, and the answer is the same: your changes are not visible to mmap until you call <code>m.flush()</code> or <code>m.close()</code>.
If you want to avoid having to call <code>m.flush()</code> manually, you can try using the <code>mmap.MAP_SHARED</code> flag when you create the mmap, which will ensure that mmap changes are written to disk immediately.

