import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'1')
    m.write(b'3')
</code>
But it gives the error <code>OSError: [Errno 22] Invalid argument</code>
From the Python documentation:
<blockquote>
<p>Updating a file only needs read access to the original file, but truncating it needs write access.</p>
</blockquote>
What am I doing wrong?


A:

<code>m = mmap.mmap(f.fileno(), 0)
</code>
is wrong, as you have already opened <code>f</code> and you have a default file size of 1 byte.
You need to pass the maximum file size to memory map it.
<code>m = mmap.mmap(f.fileno(), mmap.PAGESIZE)
</code>
this will map length equal to mmap.PAGESIZE (4096 bytes on Windows and most Linuxes)

