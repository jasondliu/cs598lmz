import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be an empty byte array, but it's not. I would like to know why this is happening and what is the correct way to clear a mmap object.


A:

<code>mmap</code> is not a list of bytes. It is a memory-mapped file. It is a way to access a file as if it was in memory. It does not know about the file's size.
<code>mmap</code> is a very low-level tool. You can use <code>mmap.resize</code> to truncate the file (and the <code>mmap</code>), but you have to know the size of the file.
You can also use <code>mmap.resize</code> to expand the file (and the <code>mmap</code>).
You can use <code>mmap.move</code> to move the file (and the <code>mmap</code>).
You can use <code>mmap.close</code> to close the file (and the <code>mmap</code>).

