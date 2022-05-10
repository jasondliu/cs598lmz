import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I would expect that the mmap object is still valid after truncating the file.
Is there a way to truncate the file and keep the mmap object valid?

