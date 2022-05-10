import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I know that I can use <code>mmap.resize</code> to fix this, but I want to know why this error is raised.
I think that <code>mmap</code> should be aware of the file size, but it seems that it is not.
Is there any way to make <code>mmap</code> aware of the file size?


A:

The <code>mmap</code> object is not aware of the file size. It is a view of the file, and it is not updated when the file is truncated.
The <code>mmap</code> object is not aware of the file size, but it is aware of the size of the memory-mapped region.
The <code>mmap</code> object is not aware of the file size, but it is aware of the size of the memory-mapped region.
The <code>mmap</code> object is not aware of the file size, but it is aware of the size of the memory-mapped region.
The <
