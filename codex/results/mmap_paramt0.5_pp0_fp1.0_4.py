import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.flush()
    m.close()
</code>
The documentation for the <code>flush</code> method says:
<blockquote>
<p>Write any changes made to the mapping back to the underlying file.</p>
</blockquote>
However, if I run the program, the file size is still 1 byte.
Why is that?


A:

The problem is that you are using <code>mmap.mmap</code> with a size of 0.  This means that you are mapping the entire file into memory.  The problem is that the file is only 1 byte long, so you are mapping that one byte.  When you write to that byte, you are modifying the copy of the byte in memory, not the byte in the file.
If you change the size of the map to something larger, then the changes to the file are visible.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mm
