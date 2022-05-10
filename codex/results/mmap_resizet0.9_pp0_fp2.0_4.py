import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
produces
<code>OSError: [Errno 2] No such file or directory
</code>
but no problems if I split the file object and mmap object operations into two separate blocks.
This issue is seen on both Python 2.7 and Python 3.4, on Linux and on Mac. I'm using Debian testing and OS X 10.9.


A:

This is behaving in a very OS specific way. If you consider what is actually happening it's easy to see why it's failing. When you do <code>f.truncate()</code>, the kernel basically resets the file to have 0 bytes and then you do <code>m[:]</code> which is asking the kernel to return bytes 1 through infinity of the file (since <code>mmap</code> uses the same <code>read</code> syscall that your <code>open</code> and <code>file</code> objects use). On Linux, this is a no-op and it's why your code works there. This is because it is the responsibility of the caller (in this case your program) to respect the bounds of the <code
