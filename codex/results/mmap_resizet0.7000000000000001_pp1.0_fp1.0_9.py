import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

    Traceback (most recent call last):
        File "./test.py", line 10, in &lt;module&gt;
        a = m[:]
    ValueError: mmap offset is greater than file size
</code>
You can see that the mmap object is still pointing to the file that has been truncated.
I need to know if there is any way to force the mmap object to not point to the underlying file and just return an empty list when I try to read the mmap object.


A:

You need to <code>munmap</code> the mmap object before closing the file.  This will cause all copies of the memory map to be removed.

