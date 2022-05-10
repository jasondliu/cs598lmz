import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think it's because <code>mmap.mmap</code> uses <code>lseek</code> to get the file size, and <code>lseek</code> returns the old file size.
Is there a way to make <code>mmap</code> work with a truncated file?


A:

You can use <code>mmap.resize</code> to resize the mapping after the file has been truncated.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
</code>

