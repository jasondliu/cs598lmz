import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m.read()
    c = m.read(1)
    m.seek(0)
    d = m[:]
    e = m.read()
</code>
This is the traceback I get.
<code>Traceback (most recent call last):
  File "mmap_test.py", line 18, in &lt;module&gt;
    e = m.read()
ValueError: read of closed file
</code>
I would expect a,b and c to return the empty string and a, b, c and d to be equal. Also I would expect m to be closed after f.truncate(), since it is the last reference to that file.


A:

I managed to find out why I was getting a <code>ValueError</code> when trying to read from the <code>mmap</code> object. Since the underlying <code>file</code> object is truncated, it is closed, causing the <code>ValueError</code>.
The docs are unclear on whether or not the <code>mmap</code> object keeps a reference to the <code>
