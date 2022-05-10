import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives me a <code>ValueError: mmap offset is greater than file size</code>.
I know that I can use <code>mmap.resize</code> to resize the mmap, but I don't know how to get the new size of the file.
I also know that I can use <code>mmap.resize</code> to resize the mmap to a size that is larger than the file, but I don't know how to get the new size of the file.
I also know that I can use <code>mmap.resize</code> to resize the mmap to a size that is larger than the file, and then use <code>mmap.move</code> to move the mmap to the end of the file, but I don't know how to get the new size of the file.
I also know that I can use <code>mmap.resize</code> to resize the mmap to a size that is larger than the file, and then use <code>mmap.move</code> to move the mmap to the end of the file, and then use <code>mmap.
