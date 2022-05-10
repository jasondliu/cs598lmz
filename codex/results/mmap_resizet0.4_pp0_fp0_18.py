import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get <code>ValueError: mmap offset is greater than file size</code> on the last line.
I guess this is because the file size is 0, but I don't understand why.
I thought that the <code>mmap</code> object would be "frozen" at the time of creation and would not change when the underlying file is modified.

