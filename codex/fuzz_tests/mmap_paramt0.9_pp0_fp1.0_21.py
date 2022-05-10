import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1)
    m.close()
</code>
The line <code>m.resize(1)</code> causes an error. The file is then truncated to 0 bytes in size.
<code>mmap.error: [Errno 22] Invalid argument
</code>
I'm guessing that mmap is not supported for python files, but I'm not clear on what the limitations are, or if there is a workaround.


A:

<blockquote>
<p>This operation is only valid for buffers of file-like objects that are using an operating-system file.</p>
</blockquote>
http://docs.python.org/2/library/mmap.html#mmap.mmap
So your mmap will only work if you have a file on actual disk.

