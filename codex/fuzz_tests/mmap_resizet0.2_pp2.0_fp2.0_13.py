import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the mmap object is not aware of the file truncation, but I don't understand why it is not.
I also tried to use <code>mmap.resize</code> but it doesn't work either.
Is there a way to make it work?


A:

The problem is that the mmap object is not aware of the file truncation.
The solution is to close the mmap object before truncating the file.

