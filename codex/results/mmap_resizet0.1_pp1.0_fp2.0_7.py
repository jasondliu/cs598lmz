import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I can't understand why.
I think that <code>m[:]</code> should return empty bytes.
But it raises exception.
Why?


A:

The <code>mmap</code> object is a view of the file, and it doesn't change when you truncate the file.
The <code>mmap</code> object is still pointing to the same bytes in the file, but the file is now shorter, so the bytes are no longer there.

