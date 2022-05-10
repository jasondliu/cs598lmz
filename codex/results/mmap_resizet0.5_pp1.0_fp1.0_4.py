import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Here, <code>m</code> is a mmap object, and <code>f</code> is a file object. The mmap object is created with <code>f.fileno()</code>, i.e. the file descriptor of the file object.
I expect that the <code>m[:]</code> should throw an exception, because the file object has been truncated, and the mmap object is still pointing to the old file.
However, it does not. The <code>m[:]</code> returns b'\x01', which is the correct content of the file before truncation.
I am wondering why it works?


A:

The mmap object is a memory map of the file. It does not have any knowledge of the file object, and is not affected by changes to the file object.

