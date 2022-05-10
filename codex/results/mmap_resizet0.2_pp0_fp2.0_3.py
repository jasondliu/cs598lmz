import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Windows, but on Linux I get <code>ValueError: mmap offset is greater than file size</code>.
I think the problem is that <code>truncate</code> doesn't actually change the file size until the file is closed.  Is there a way to make this work on Linux?


A:

I think you're right about the problem.  I don't know of a way to make this work on Linux.  I think you'll have to close the file, truncate it, and then reopen it.

