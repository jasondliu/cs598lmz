import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
This code will crash with <code>ValueError: mmap offset is greater than file size</code>. The problem is that the file size is now 0, but the offset is still 1.
Is there a way to get a mmap object that is valid even after the file is truncated?

