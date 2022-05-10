import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm getting <code>ValueError: mmap offset is greater than file size</code>.
I've read that <code>mmap</code> is not compatible with <code>truncate</code> but I don't understand why.
I'm on Python 3.6.5.


A:

<code>mmap</code> is a wrapper around the operating system's memory-mapped file API.  It's not a Python object.  It doesn't know anything about the file object it's associated with.  It's just a pointer to a memory region.  If you <code>truncate</code> the file, you've invalidated the pointer.
If you want to use <code>mmap</code> with a file that might be truncated, you have to keep track of the original file size and use that to determine the length of the mapped region.  You can't use <code>mmap.mmap.size</code> for this because that's the size of the mapped region, not the size of the file.

