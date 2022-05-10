import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises a <code>ValueError: mmap offset is greater than file size</code>.
Is there a way to get the data from the <code>mmap</code> object after the file has been truncated?

