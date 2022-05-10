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
I get <code>b'\x00'</code> instead of <code>b'\x01'</code>.
How can I get the previous value?
I'm using Python 3.6.1 on Ubuntu 17.04.


A:

When you truncate the file, the file is resized and the bytes after the new end of the file are discarded.
The mmap object is still "mapped" to the old size.  If you try to access the byte after the new end of the file, you get the byte at offset 0.

