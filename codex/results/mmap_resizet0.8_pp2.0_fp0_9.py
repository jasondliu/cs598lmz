import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This throws: <code>ValueError: mmap offset is greater than file size</code>
I understand the reason for this and that mmap will still think it is pointing to the first position. What I don't understand is why is the mmap still active when the file has been truncated?


A:

The <code>mmap</code> instance is mapping the original file, not the contents. It doesn't know about any changes made to the file after it was opened.
Generally, <code>mmap</code> would only be used to read a file, not to write a file.

