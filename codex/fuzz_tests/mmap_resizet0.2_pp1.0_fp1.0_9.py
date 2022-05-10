import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I would expect that the <code>mmap</code> object would be updated to reflect the new file size.
Is there a way to get this to work?


A:

<code>mmap</code> is not a file object. It is a memory-mapped view of the file.
<code>mmap</code> does not know about the file object.
<code>mmap</code> does not know about the file size.
<code>mmap</code> does not know about the file name.
<code>mmap</code> does not know about the file descriptor.
<code>mmap</code> does not know about the file.
<code>mmap</code> is a memory-mapped view of the file.
<code>mmap</code> is not a file object.
<code>mmap</code> is not a file object.
<code>mmap</code> is not a file object.
<code>mmap</code> is not a file
