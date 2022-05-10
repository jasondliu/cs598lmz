import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    print(m.read(1))
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.close()
</code>


A:

<code>mmap</code> is a wrapper around the <code>mmap</code> system call, which maps a file into memory.  When you resize the file, the system call is still using the old size.  The <code>mmap</code> call doesn't know that the file has been resized, so it doesn't know to re-map the file.
You can unmap the file with <code>m.close()</code>, then re-map it with <code>m = mmap.mmap(f.fileno(), 0)</code> to get the new size.

