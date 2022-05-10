import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error:
<code>mmap.error: [Errno 22] Invalid argument
</code>
I know I can get around this by using <code>mmap.ACCESS_READ</code> when creating the mmap, but I don't want to do that.  Is there a way to do this?


A:

You can't use <code>mmap</code> to read from a file that has been truncated. You can use <code>mmap</code> to write to a file that has been truncated, but not to read from it.

