import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Why does this print <code>b'\x01'</code>? I would expect this to raise an <code>OSError</code> because the file was truncated.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>If length is larger than the current size of the file, the file is extended to contain length bytes.</p>
</blockquote>
So the file is extended to the size of the <code>mmap</code> object and the contents of the <code>mmap</code> object are unchanged.

