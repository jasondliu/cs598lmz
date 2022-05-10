import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code fails with <code>ValueError: mmap offset is greater than file size</code>.
I am not sure why this happens. The file is opened in read/write mode, so shouldn't the mmap object be able to read from the file even if the file is truncated?
I am using python 3.5.2 on Linux.


A:

The <code>mmap</code> object is not aware of the file being truncated. The <code>mmap</code> object was created with a map size of 0, which means it will map the whole file. The file has now been truncated to 0, so the <code>mmap</code> object can't map it.

