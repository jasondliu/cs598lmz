import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I'm using Python 3.6.8.


A:

<blockquote>
<p>The last line raises ValueError: mmap offset is greater than file size.</p>
</blockquote>
This is because you're using the <code>m[:]</code> syntax, which is equivalent to <code>m[0:len(m)]</code>.
The problem is that <code>len(m)</code> returns the length of the memory-mapped file when it was first opened, not the current length of the file.
The solution is to use <code>m[0:]</code> instead, which will return the entire memory-mapped file, no matter how long it is.

