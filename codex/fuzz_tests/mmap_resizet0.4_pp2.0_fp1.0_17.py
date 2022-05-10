import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
It raises <code>ValueError: mmap offset is greater than file size</code>.
I know that I can use <code>mmap.resize(0)</code> to avoid this error, but I wonder why <code>mmap</code> doesn't update its offset automatically.


A:

<code>mmap</code> is a wrapper around the <code>mmap</code> system call. The <code>mmap</code> system call maps a file into memory, and it's up to the kernel to decide how to do that.
The kernel could map the file in its entirety, but that would mean that the kernel would have to allocate memory for the entire file. It would also mean that the kernel would have to check the file size every time a page fault occurs, to make sure that the file hasn't been truncated.
Instead, the kernel maps the file in chunks. When the kernel needs to map a chunk, it checks the file size and maps the chunk up to the end of the file. This means that the kernel doesn't need to allocate memory for the entire file, and it doesn't need to check
