import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line gives me a <code>ValueError: mmap closed or invalid</code>.
I tried to do it in two steps:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    m.close()
</code>
But it gives me an <code>OSError: [Errno 22] Invalid argument</code>.
How can I read from a mmap after truncating the file?


A:

<code>mmap</code> is a view of the underlying file.  When you truncate the file, you're changing the size of the file.  The <code>mmap</code> is still a view of the original file, which is now smaller than the <code>mmap</code> thinks it is.
You need to
