import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
the last line throws <code>ValueError: mmap offset is greater than file size</code>. The error is caused by <code>f.truncate()</code>. If I remove that line, the code works fine.
I thought I could truncate the file and then mmap the new file size. But that doesn't seem to work. Does this mean that <code>mmap</code> doesn't work after truncating a file?
I am using Python 3.6.


A:

The <code>mmap</code> module is about mapping a file into memory.
The <code>mmap</code> object is created by mapping a file into memory.
The memory is mapped to the file and the memory mapping is not aware of changes made to the file.
<code>f.truncate()</code> changes the file size.
The <code>mmap</code> object is still mapped to the original file size.
If you want to map the full file, you need to create a new <code>mmap</code> object.
If you want to map a part of the file, you need to create
