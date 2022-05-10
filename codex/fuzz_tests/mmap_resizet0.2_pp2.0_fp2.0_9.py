import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code throws <code>ValueError: mmap offset is greater than file size</code> exception.
I know that I can use <code>mmap.resize</code> method to fix this problem, but I want to know why this exception is thrown.
I think that <code>m[:]</code> should return empty bytes object, but it doesn't.


A:

The <code>mmap</code> object is a view into the file, and it can't be resized.  It's not a copy of the file.  If you want to read the entire file, you can use <code>m.read()</code>.  If you want to read the entire file into a <code>bytes</code> object, you can use <code>m.read_byte()</code>.

