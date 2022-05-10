import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the mmap object is no longer valid after the truncate, but I would expect it to raise an error when I try to access it.
Is there a way to get an error when I try to access the mmap object after the truncate?


A:

You can't. The mmap object is no longer valid after the truncate, but you can't tell.
The mmap object is just a wrapper around a pointer to a memory-mapped region of the file. After the truncate, the memory-mapped region is still there, but it doesn't point to the file anymore.

