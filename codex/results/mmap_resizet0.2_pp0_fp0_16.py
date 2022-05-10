import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file size is 0, but I don't understand why the mmap is not updated.
Is there a way to make the mmap aware of the file truncation?


A:

The <code>mmap</code> object is not aware of the file truncation because the <code>mmap</code> object is not aware of the file.
The <code>mmap</code> object is a wrapper around a memory-mapped file.  The memory-mapped file is created by the operating system, and is not aware of the file.  The memory-mapped file is a mapping of the file's contents into memory, and is not aware of the file.  The memory-mapped file is not aware of the file.
The <code>mmap</code> object is a wrapper around the memory-mapped file.  The <code>mmap</code> object is not aware of the file.
When you truncate the file, the file is truncated.  The memory-mapped file is not trunc
