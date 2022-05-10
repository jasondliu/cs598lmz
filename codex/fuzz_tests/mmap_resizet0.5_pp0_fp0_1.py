import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Is there a way to get the contents of the file before it was truncated?


A:

You can't do this with Python's <code>mmap</code> module. 
<code>mmap</code> maps the file into memory, so any changes to the file are immediately reflected in the memory mapping. If you truncate the file, the memory mapping is reduced to the new size of the file.

