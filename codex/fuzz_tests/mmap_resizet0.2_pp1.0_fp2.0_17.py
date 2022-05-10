import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code fails with <code>ValueError: mmap offset is greater than file size</code>.
I know that I can use <code>mmap.resize</code> to resize the mmap, but I don't want to do that. I want to truncate the file and then read the mmap.
The only way I found to do this is to close the file, reopen it and then read the mmap.
Is there a way to do this without closing the file?


A:

You can't. The <code>mmap</code> object is tied to the file descriptor, and the file descriptor is tied to the file.

