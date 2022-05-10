import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This will raise a <code>ValueError: mmap offset is greater than file size</code>.
I would expect the <code>mmap</code> object to be updated to reflect the truncation.
Is this a bug or am I missing something?


A:

The <code>mmap</code> object is updated to reflect the truncation.
The <code>ValueError</code> is raised because the <code>mmap</code> object is updated to reflect the truncation.
The <code>mmap</code> object is not a copy of the file, it's a view of the file. 
The <code>mmap</code> object is updated to reflect the truncation.

