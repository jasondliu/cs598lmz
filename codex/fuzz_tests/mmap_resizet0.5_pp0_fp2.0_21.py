import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
If I comment it out, the program runs without errors.
What's going on here?


A:

<code>mmap</code> is a memory-mapping interface, it doesn't actually read the file contents into memory. It just maps the file contents into the process' address space.
When you call <code>f.truncate()</code>, you truncate the file to zero bytes. The file has no contents, so there is nothing to map.

