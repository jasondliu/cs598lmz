import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws a <code>ValueError: mmap offset is greater than file size</code>.
I would expect that the <code>mmap</code> object would be updated to reflect the truncation.
Is there a way to do this?


A:

I think you need to close the mmap object before truncating the file.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>

