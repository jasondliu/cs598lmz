import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>. 
So I think the underlying file is truncated when <code>f.truncate()</code> is executed.
But why <code>m[:]</code> still returns <code>b'\x00'</code>?


A:

The <code>mmap</code> object is not updated when you truncate the file. The documentation says:
<blockquote>
<p>If the file is resized via ftruncate(2) or another mechanism, the contents of the resized portion are undefined.</p>
</blockquote>

