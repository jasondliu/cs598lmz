import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = b'a'
</code>
This works as expected, but when I try to use <code>m</code> after <code>f</code> has been closed, I get a <code>ValueError</code> saying <code>mmap: cannot find the file</code>. If I don't close <code>f</code>, then <code>m</code> works fine.
How can I use the <code>mmap</code> object after the file has been closed?


A:

The problem is that the C-level file descriptor is closed when the file is closed, which is what the OS uses to keep track of the file.
But you can easily work around this by keeping the file open, and using <code>fileno()</code> to get a new file descriptor that refers to the same file.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.
