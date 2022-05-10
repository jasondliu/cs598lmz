import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives me an error:
<blockquote>
<p>FileNotFoundError: [Errno 2] No such file or directory</p>
</blockquote>
How can I get mmap to work after truncation?


A:

The error is being thrown because the file referenced by the mmap, <code>f.fileno()</code>, is no longer available since it was truncated.  There's not much that can be done after that, since the file is no longer there. 

