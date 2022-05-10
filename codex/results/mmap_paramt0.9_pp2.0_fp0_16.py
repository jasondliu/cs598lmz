import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 'a'
    m[1] = b'a'
</code>
The following error was issued:
<code>cannot read or write from this mmap - it is already closed
</code>


A:

The error message is misleading -- the mmap object has not yet been closed, nor is it ever closed (at least when you use context manager to open the file).  
The problem is that you have exceeded the size of memory-mapped file.  Memory-mapped files cannot grow arbitrarily; if you try to write to an offset beyond the existing EOF, the write fails and the object gets "closed".  This is by design.
Because the object has been closed, but you've still got the reference, you see this error.
You can work around the issue by growing the underlying file to the appropriate size before hitting the error:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f
