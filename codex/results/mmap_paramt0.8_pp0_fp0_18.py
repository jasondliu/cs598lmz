import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
</code>
This is on Windows 7 and Python 3.8.1 and I'm using the 64-bit build of Python.


A:

This is seen on Python 3.8.1 on Windows and Python 3.7.5 on Linux.
The reason is that the Windows implementation of <code>mmap.mmap</code> will silently fix the <code>length</code> argument if it's <code>0</code>.  This causes the 0-byte file to be mapped to all bytes of length <code>0x7FFFFFFF</code>.  This is not an issue on Linux, which pre-allocates the file to the given size.
As a workaround, use <code>length = os.stat(filename).st_size</code> to get the file size.
I've submitted a bug report for this: https://bugs.python.org/issue39966

