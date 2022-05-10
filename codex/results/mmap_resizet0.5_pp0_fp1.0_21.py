import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
On Linux, this throws <code>mmap.error: [Errno 9] Bad file descriptor</code>
On Windows, this throws <code>ValueError: mmap length is zero</code>
Is there a portable way to get the contents of the file after truncation?


A:

Use <code>mmap.ACCESS_READ</code> instead of <code>0</code> to specify the access mode.

