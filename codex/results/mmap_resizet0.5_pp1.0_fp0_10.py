import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
I would expect the output to be <code>b''</code>, but it is <code>b'\x01'</code>.
I am using Python 3.6.1 on Windows 10.


A:

This is not a bug, it's a feature.
The <code>mmap</code> object is not tied to the file. It is tied to the file descriptor. The file descriptor is tied to the file.
The <code>truncate</code> call only truncates the file, not the file descriptor. The file descriptor is still valid, and the <code>mmap</code> object is still valid.

