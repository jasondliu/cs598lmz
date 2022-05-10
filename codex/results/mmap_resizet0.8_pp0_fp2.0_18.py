import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
output:
<code>b'\x01'
</code>
but if I replace <code>f.truncate()</code> with <code>m.resize(0)</code>, <code>m[:]</code> returns <code>b''</code>, the value before the truncate.
I expected <code>m.resize(0)</code> to affect the mmap object, but it seems like it doesn't. Why is that?


A:

<code>mmap.mmap.resize</code> is a method that tells the OS to shrink the mapped region.  It doesn't call <code>truncate</code> on the backing file.
From the documentation:
<blockquote>
<p>If length is less than the current map size, the map is reduced to length bytes.  The contents of the removed portion are lost.</p>
</blockquote>

