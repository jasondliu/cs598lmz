import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expected the output to be <code>b'\x01'</code>, but instead I got <code>b''</code>.
I have also tried using <code>mmap.ACCESS_READ</code> and <code>mmap.ACCESS_WRITE</code> instead of <code>mmap.ACCESS_COPY</code>, but the result was the same.
I am using Python 3.6.1 on Windows 10.


A:

The problem is that the <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap() function may need to update the internal mapping between virtual memory and files. This is done by the msync() function, which is called automatically when needed.</p>
</blockquote>
But it doesn't say when it is needed.
The solution is to call <code>m.resize(0)</code> after truncating the file.

