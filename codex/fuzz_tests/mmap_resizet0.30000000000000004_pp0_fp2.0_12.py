import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code raises <code>ValueError: mmap closed or invalid</code> exception.
I know that I can use <code>mmap.ACCESS_WRITE</code> flag to avoid this error. But I want to know why this error occurs.
Is it because of <code>mmap</code> object is not updated after <code>truncate</code>?

