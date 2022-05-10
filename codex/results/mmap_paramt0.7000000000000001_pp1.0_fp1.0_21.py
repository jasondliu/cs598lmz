import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>


A:

The <code>mmap.mmap</code> constructor takes a <code>length</code> parameter that you're passing as <code>0</code>.  If <code>length</code> is <code>0</code>, then the length is taken from the length of the file.  Since your file is only one byte long, <code>m[0] = b'\x00'</code> is out of bounds.  You should use <code>mmap.mmap(f.fileno(), 1)</code> instead.

