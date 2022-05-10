import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws a <code>ValueError: mmap offset is greater than file size</code>.
My understanding is that the <code>mmap</code> object is invalid after the file is truncated, but I think it shouldn't be a problem if I don't try to access it.
Is this a bug in Python 3.6.5? 

