import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap closed or invalid</code>.
Is it possible to use file with <code>mmap</code> if file is truncated?


A:

The problem is that when you created the <code>mmap</code>, you told Python it could be of any size. When you call <code>f.truncate()</code>, it removes all the rest of the file, so there's nothing for your <code>mmap</code> to point to.
You need to <code>resize</code> the <code>mmap</code> object before you can use it again:
<code>f.truncate()
m.resize(0)
a = m[:]
</code>
Or you could call <code>resize</code> before you call <code>truncate</code>, but that's not as straightforward:
<code>m.resize(0)
f.seek(0)
f.truncate()
</code>
Note that the <code>m.resize()</code> method is documented in Python
