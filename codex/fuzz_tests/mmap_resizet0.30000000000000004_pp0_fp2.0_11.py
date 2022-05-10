import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises <code>ValueError: mmap offset is greater than file size</code>.
I have a program that uses <code>mmap</code> to access a file. I want to be able to truncate the file and still be able to access the contents of the file before it was truncated.
Is there any way to do this?


A:

You can't do this.  The mmap object is a view into the file.  When you truncate the file, the mmap object is no longer valid.

