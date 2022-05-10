import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code> exception.
I think it's because <code>mmap</code> object is not aware of the file size change.
Is there any way to make <code>mmap</code> object aware of the file size change?
Or is there any way to truncate file without raising exception?

