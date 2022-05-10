import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think it is because <code>m</code> is not updated after <code>f.truncate()</code>.
How can I update <code>m</code>?


A:

You can't.
The <code>mmap</code> object is a view into the file, and it can't be updated when the file is truncated.
You'll have to close the <code>mmap</code> object and re-open it.

