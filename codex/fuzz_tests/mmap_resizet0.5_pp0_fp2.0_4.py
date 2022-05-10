import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line of the code above raises <code>ValueError: mmap offset is greater than file size</code>.
I think the reason is that the mmap object is not updated when the file is truncated.
How can I update the mmap object after the file is truncated?

