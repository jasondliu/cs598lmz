import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I know that <code>mmap</code> is not a good idea for writing, but I need to use it.
Is there any way to avoid this exception?


A:

You can't use <code>mmap</code> to write to a file that has been truncated.
<code>mmap</code> is a memory-mapped file.  It is a way to access the contents of a file as if it were in memory.  When you truncate the file, the memory-mapped file is no longer valid.
If you want to write to a file, you need to use the <code>write</code> method of the file object.  If you want to read from a file, you need to use the <code>read</code> method of the file object.

