import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code throws <code>ValueError: mmap offset is greater than file size</code> on the last line.
I understand that the file is truncated and the mmap is no longer valid. But why does it throw an exception?
I would expect the code to return an empty byte array.

