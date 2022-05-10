import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x01'</code>, but I expected it to be <code>b''</code>.
I'm using Python 3.6.1 on Windows 10.


A:

The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</
