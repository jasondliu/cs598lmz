import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line of the code throws <code>mmap.error: [Errno 22] Invalid argument</code>.
I understand that the <code>mmap</code> object is no longer valid after the file is truncated, but I don't understand why. I thought that the <code>mmap</code> object is just a view of the file, and the file is still valid.
I am using Python 3.6.8 on Windows 10.


A:

<blockquote>
<p>I thought that the mmap object is just a view of the file, and the file is still valid.</p>
</blockquote>
That's true, but the <code>mmap</code> object is not just a view of the file, it's a view of a specific range of the file.
In your case, you're mapping the whole file, so the <code>mmap</code> object is a view of the whole file. But when you truncate the file, the <code>mmap</code> object is still a view of the whole file, which is now smaller than it was before.

