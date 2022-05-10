import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This fails with <code>ValueError: mmap offset is greater than file size</code>.
The problem is that mmap does not know that the file has been truncated.
How can I get mmap to know that the file has been truncated?
(I know that I can read the file with <code>mmap.ACCESS_READ</code> but I want to know if there is a way to get this to work with <code>mmap.ACCESS_WRITE</code>.)

