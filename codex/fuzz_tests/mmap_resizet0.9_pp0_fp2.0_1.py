import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

&gt;&gt;&gt; a
b''
</code>
Is there a way to access the remaining part of the file?


A:

mmap updates its internal information when you close it. If you want to change the size of the internal mapping, you'll either have to close it and reopen it, or create a new one on a file opened in append-only mode. The astute might notice that the latter trick doesn't really resize the file in-place; this is a general restriction of memory mapped files: in Python you cannot resize a memory mapped file that you're also changing its content (mmap in posix doesn't even allow you to resize if you can't write to it).
This might also be implementation specific, check the docs and the source code yourself.

