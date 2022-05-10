import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line gives an error:
<code>mmap.error: [Errno 22] Invalid argument
</code>
Why?
I am using Python 3.5.2 on Linux.


A:

<code>mmap</code> requires a file with a known size. When you truncate the file, the <code>mmap</code> object is no longer valid.
You need to <code>close</code> the <code>mmap</code> object before truncating the file.

