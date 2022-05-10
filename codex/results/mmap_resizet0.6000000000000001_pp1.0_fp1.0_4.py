import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It raises <code>ValueError: mmap offset is greater than file size</code>.
This is expected because the file is truncated. But what I'm wondering, is if there is a way to keep the mmap valid, but with the new file size. I couldn't find any method in the mmap object that does this.
My use case is that I have a file with a header and a footer, and a variable size body in the middle. I'm memory mapping the file, and reading the header and footer directly. I'd like to be able to update the body, and then change the file size (and the mmap size) accordingly.

