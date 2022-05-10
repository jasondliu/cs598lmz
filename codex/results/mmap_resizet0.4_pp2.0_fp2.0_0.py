import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I think the reason is that the mmap object is not updated after the truncate.
Is there a way to update it?


A:

The <code>mmap</code> module is not designed to work with files that are truncated. You should <code>mmap</code> the file before truncating it.

