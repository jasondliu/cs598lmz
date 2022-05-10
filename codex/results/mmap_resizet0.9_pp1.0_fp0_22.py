import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<blockquote>
<p>mmap.error: [Errno 12] Cannot allocate memory</p>
</blockquote>
The only solution I found was to use <code>mmap.RESIZEABLE</code> which would require me to re-open the file after resizing, but it really bothers me I cannot get a real answer for this issue.
Why is reading the mmap file resulting in an error after resizing the backing file?
(Windows 10, python 3.7.3, memory mapped in shared mode)

