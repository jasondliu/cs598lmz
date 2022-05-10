import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code will raise <code>ValueError: mmap offset is greater than file size</code> on the last line.
Is there a way to truncate a file and still be able to read from the mmap?


A:

No, there is no way to truncate a file and still be able to read from the mmap.
The reason is that the mmap object is not aware of the truncation.
You can work around it by doing the truncation before creating the mmap object.

