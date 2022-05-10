import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives me a <code>mmap.error: [Errno 22] Invalid argument</code>. It also happens if I use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> or <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)</code>.
Is it possible to truncate the file after mmap-ing it?
I am using Python 3.7.1 in Windows 10.


A:

It is possible to resize the file, but the <code>mmap</code> object is still referring to the original size of the file.
If you want to access the data in the new file, you need to <code>mmap</code> it again.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate
