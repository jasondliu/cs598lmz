import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think it's because <code>truncate</code> doesn't change the file size immediately.
How can I truncate a file and keep the mmap object valid?


A:

You can't.
The mmap object is a view of the file, and the file is truncated.
You can't have a view of a file that is larger than the file.

