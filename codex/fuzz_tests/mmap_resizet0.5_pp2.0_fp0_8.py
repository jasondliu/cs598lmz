import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
This code throws an <code>mmap.error: [Errno 22] Invalid argument</code>. I believe this is because the underlying file descriptor has been truncated.
I tried to replace the <code>truncate()</code> call with <code>os.ftruncate(f.fileno(), 0)</code>, but this throws a <code>ValueError: can't have unbuffered text I/O</code> in Python 3.6.
I'm using Python 3.6.1 on Windows 10.


A:

It's not possible to truncate the underlying file while the <code>mmap</code> object is open. This is because the <code>mmap</code> object holds a file descriptor to the file, and truncating the file invalidates that file descriptor.
The solution is to close the <code>mmap</code> object before truncating the file.

