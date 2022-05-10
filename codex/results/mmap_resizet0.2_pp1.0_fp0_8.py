import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file size is 0 after <code>truncate</code>, but why does the <code>mmap</code> object still think that the file size is 1?


A:

<code>mmap</code> is a wrapper around the <code>mmap</code> system call.  The <code>mmap</code> system call is documented in the <code>mmap(2)</code> man page.  The <code>mmap</code> system call is not a wrapper around <code>open</code> and <code>read</code> system calls.  It is a wrapper around the <code>mmap</code> system call.  The <code>mmap</code> system call does not read the file.  It maps the file into memory.  The <code>mmap</code> system call does not change the file size.  It maps the file into memory.
The <code>mmap</code> system call does not change the file size.  It maps the file into
