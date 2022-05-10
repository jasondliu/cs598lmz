import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
But <code>m[:]</code> is not <code>b''</code> (as expected) but <code>b'\x00'</code>.
How can I fix this behaviour?


A:

I could not find the exact reason of this behavior. 
I think the OS has not updated the file size in the filesystem yet, but has updated the size in the memory cache. Maybe there is a tiny period of time, where the OS has not yet updated the size of the file on the disk.
But this is just a guess.
You could use the <code>m.resize</code> function to adjust the size of the mmap object, which will leave the mmap object in a valid state. In your case, this would be:
<code>m.resize(0)
</code>
In general, the resize function does not have any effect on the actual file size. It only resizes the mmap object.

