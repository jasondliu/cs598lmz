import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # raises `ValueError: mmap can't resize memory maps backed by files`
</code>
I've read that this is because the <code>mmap</code> doesn't know what's going on behind it, but I don't understand why? If the file was truncated, shouldn't the <code>mmap</code> know and reflect this?
EDIT:
This works if the <code>mmap</code> is created before the file is truncated. But what if the file is truncated before the mmap is created?
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>


A:

Your question is rather generic, and I'm not entirely sure what you're asking.
The mmap module is meant to map a file on disk into a segment of memory. It is not meant to be a general-purpose file wrapper. It is meant to be a tool
