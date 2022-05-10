import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws <code>IndexError: memory mapping has been closed</code>.
If I comment out <code>f.truncate()</code> line, it doesn't throw an error.
I read, that memory mapping doesn't change after file is truncated and I think it's the reason for this exception.
But, I don't understand, why does it happen?
<code>m[:]</code> doesn't return a copy of the memory mapping, it returns a slice of the file, and the file hasn't changed. I thought it should work, because the file hasn't changed.
My OS is Linux, Python version is 3.5.

