import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Linux, but on Windows it raises <code>ValueError: mmap offset is greater than file size</code>.
I know that I can use <code>m.resize(0)</code> instead of <code>f.truncate()</code>, but I want to know why this code works on Linux and not on Windows.


A:

The <code>mmap</code> module is a wrapper around the <code>mmap()</code> system call. The <code>mmap()</code> system call is documented in the <code>mmap(2)</code> man page on Linux, and in the <code>mmap(2)</code> man page on macOS.
The <code>mmap()</code> system call is documented in the <code>mmap(2)</code> man page on Linux, and in the <code>mmap(2)</code> man page on macOS.
The <code>mmap()</code> system call is documented in the <code>mmap(2)</code> man page on Linux, and in the <code>mmap(
