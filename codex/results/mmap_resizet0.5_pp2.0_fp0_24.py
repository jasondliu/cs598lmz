import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line of this code throws an exception:
<code>ValueError: mmap offset is greater than file size
</code>
How can I truncate the file without invalidating the mmap?


A:

It's not possible to truncate a file if the file is mapped.
From the <code>mmap</code> documentation:
<blockquote>
<p>Note that modifications to the file while it is mapped are not reflected in the contents of the array until the file is unmapped.</p>
</blockquote>
The file must be unmapped before it can be truncated.

