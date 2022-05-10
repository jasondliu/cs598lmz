import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # mmap.error: cannot extend memory mapped files
</code>
What happens? Why does the <code>m[:]</code> access throw an exception?
I am looking for a way to get the contents of the file (or a part of the file) that is being mapped without having to truncate the file first.

