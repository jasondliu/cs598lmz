import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expected this code to throw an exception, but it seems to work.
I'm running Python 3.6.5 on Ubuntu 18.04.
Is there a way to force an exception to be raised?


A:

The documentation says that if the file is truncated, the memory map will be resized (and the extra data will be lost):
<blockquote>
<p>If the file is resized, the mmap will be resized with it. If the file is enlarged, the new area is uninitialised memory. If the file is shrunk, the extra data is lost. If the file is opened read-only and its size is increased, the mmap cannot be extended to cover the new area. However, the file may be resized to a smaller size using truncate().</p>
</blockquote>
I think this is what you're seeing.

