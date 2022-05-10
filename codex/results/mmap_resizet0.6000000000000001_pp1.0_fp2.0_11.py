import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm getting an <code>BufferError</code> exception in the last line. Why is that?
Python 2.7.5


A:

<code>mmap</code> is a wrapper around the <code>mmap</code> system call.  When you truncate the file, the kernel automatically unmaps the file, and so you get the <code>BufferError</code>.

