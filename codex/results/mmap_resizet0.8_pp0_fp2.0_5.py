import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this case I receive the following error:
<blockquote>
<p>TypeError: mmap can't modify a readonly memory map</p>
</blockquote>
The documentation for <code>mmap</code> seems to indicate that a read-only file should be able to be mapped by a read-write <code>mmap</code>, but I am obviously misunderstanding something.
My current workaround is to open the file as read-write, but this feels like an unnecessary workaround.  Can anyone point me to some direction on why this doesn't work? Is the documentation in error?


A:

mmap.mmap()'s docstring:
<code>mmap(fileno, length[, flags[, prot[, access[, offset]]]])

Create a mmap object.

The arguments are:

fileno which must be an open file descriptor;
length which specifies the length of the mapping;
flags which specifies the mmap access modes;
prot which is the desired memory protection of the mapping; and
access which is the desired file access of the mapping.

These arguments correspond to the arguments
